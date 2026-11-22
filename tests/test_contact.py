"""
Tests for the contact form submission endpoint.
"""

import re
import sqlite3

import pytest
from httpx import ASGITransport, AsyncClient

from app.main import app
from app.database import get_db_path

pytestmark = pytest.mark.asyncio


VALID_CONTACT_DATA = {
    "full_name": "Jane Doe",
    "business_email": "jane@example.com",
    "company_name": "Acme Corp",
    "country": "India",
    "service_interested": "Web Development",
    "project_details": "We need a modern corporate website with a CMS.",
    "_honeypot": "",
}


async def _get_csrf_token(client) -> tuple[str, dict]:
    """
    Fetch the homepage to obtain a CSRF token from the cookie and the page.
    Returns (csrf_token, cookies_dict).
    """
    response = await client.get("/")
    csrf_cookie = response.cookies.get("csrf_token", "")

    # Also try to extract token from the hidden form field in the HTML
    match = re.search(
        r'name="csrf_token"\s+value="([^"]+)"', response.text
    )
    csrf_form_token = match.group(1) if match else csrf_cookie

    return csrf_form_token, dict(response.cookies)


async def test_contact_form_valid_submission(client):
    """POST /contact with valid data and CSRF token should redirect (302/303)."""
    csrf_token, cookies = await _get_csrf_token(client)

    data = {**VALID_CONTACT_DATA, "csrf_token": csrf_token}
    response = await client.post(
        "/contact",
        data=data,
        cookies=cookies,
        follow_redirects=False,
    )

    assert response.status_code in (302, 303), (
        f"Expected redirect, got {response.status_code}: {response.text[:300]}"
    )


async def test_contact_form_missing_fields(client):
    """POST /contact with missing required fields should show errors (200)."""
    csrf_token, cookies = await _get_csrf_token(client)

    # Submit with only CSRF token, no other fields
    data = {"csrf_token": csrf_token, "_honeypot": ""}
    response = await client.post(
        "/contact",
        data=data,
        cookies=cookies,
        follow_redirects=False,
    )

    # Should re-render the page with validation errors (not redirect)
    assert response.status_code == 200
    html = response.text.lower()
    # Check that at least one error message is present
    assert "required" in html or "error" in html or "field" in html


async def test_contact_form_invalid_email(client):
    """POST /contact with an invalid email should show an email error."""
    csrf_token, cookies = await _get_csrf_token(client)

    data = {
        **VALID_CONTACT_DATA,
        "business_email": "not-an-email",
        "csrf_token": csrf_token,
    }
    response = await client.post(
        "/contact",
        data=data,
        cookies=cookies,
        follow_redirects=False,
    )

    assert response.status_code == 200
    html = response.text.lower()
    assert "email" in html


async def test_contact_form_csrf_failure(client):
    """POST /contact without a valid CSRF token should be rejected."""
    # Submit with a bogus CSRF token and no matching cookie
    data = {**VALID_CONTACT_DATA, "csrf_token": "invalid-token-value"}
    response = await client.post(
        "/contact",
        data=data,
        follow_redirects=False,
    )

    # Should either return 403, 400, or 200 with an error — but NOT redirect
    assert response.status_code != 303
    assert response.status_code != 302


async def test_contact_form_honeypot_filled(client):
    """POST /contact with the honeypot field filled should be rejected."""
    csrf_token, cookies = await _get_csrf_token(client)

    data = {
        **VALID_CONTACT_DATA,
        "csrf_token": csrf_token,
        "_honeypot": "I am a bot filling hidden fields",
    }
    response = await client.post(
        "/contact",
        data=data,
        cookies=cookies,
        follow_redirects=False,
    )

    # Should not result in a successful redirect
    assert response.status_code != 303 or "submitted=true" not in response.headers.get(
        "location", ""
    )


async def test_contact_saves_to_database(client):
    """After a valid submission, the inquiry should exist in the SQLite database."""
    csrf_token, cookies = await _get_csrf_token(client)

    unique_name = "DB Test User"
    unique_email = "dbtest@example.com"

    data = {
        **VALID_CONTACT_DATA,
        "full_name": unique_name,
        "business_email": unique_email,
        "csrf_token": csrf_token,
    }
    response = await client.post(
        "/contact",
        data=data,
        cookies=cookies,
        follow_redirects=False,
    )

    assert response.status_code in (302, 303), (
        f"Expected redirect, got {response.status_code}"
    )

    # Query the database directly to verify the record was saved
    db_path = get_db_path()
    conn = sqlite3.connect(db_path)
    try:
        cursor = conn.execute(
            "SELECT full_name, business_email, company_name, country, "
            "service_interested, project_details FROM contact_inquiries "
            "WHERE business_email = ?",
            (unique_email,),
        )
        row = cursor.fetchone()
    finally:
        conn.close()

    assert row is not None, "Contact inquiry was not saved to the database"
    assert row[0] == unique_name
    assert row[1] == unique_email
    assert row[2] == VALID_CONTACT_DATA["company_name"]
