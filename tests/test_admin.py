"""Tests for admin dashboard routes."""

import pytest
from httpx import ASGITransport, AsyncClient

from app.main import app
from app.config import settings

pytestmark = pytest.mark.asyncio


async def test_admin_redirects_to_login_when_unauthenticated(client):
    """Accessing /admin without credentials should redirect to /admin/login."""
    response = await client.get("/admin", follow_redirects=False)
    assert response.status_code == 303
    assert "/admin/login" in response.headers["location"]


async def test_admin_login_page_renders(client):
    """GET /admin/login should return 200 with login form."""
    response = await client.get("/admin/login")
    assert response.status_code == 200
    assert "Sign In" in response.text
    assert "Username" in response.text


async def test_admin_login_invalid_credentials(client):
    """POST /admin/login with invalid password should fail with 401."""
    response = await client.post(
        "/admin/login",
        data={"username": "wrong", "password": "wrongpassword"},
        follow_redirects=False,
    )
    assert response.status_code == 401
    assert "Invalid username or password" in response.text


async def test_admin_login_valid_and_access_dashboard(client):
    """POST /admin/login with correct credentials sets cookie and allows accessing /admin."""
    # 1. Login
    login_resp = await client.post(
        "/admin/login",
        data={
            "username": settings.ADMIN_USERNAME,
            "password": settings.ADMIN_PASSWORD,
        },
        follow_redirects=False,
    )
    assert login_resp.status_code == 303
    assert login_resp.headers["location"] == "/admin"
    assert "aurocous_admin_session" in login_resp.cookies

    # 2. Access dashboard with the received cookies
    dash_resp = await client.get("/admin", cookies=dict(login_resp.cookies))
    assert dash_resp.status_code == 200
    assert "Inquiries Dashboard" in dash_resp.text
    assert "Total Inquiries" in dash_resp.text
    assert "Export to CSV" in dash_resp.text


async def test_admin_export_csv(client):
    """GET /admin/export-csv should return CSV file."""
    # Login first
    login_resp = await client.post(
        "/admin/login",
        data={
            "username": settings.ADMIN_USERNAME,
            "password": settings.ADMIN_PASSWORD,
        },
        follow_redirects=False,
    )
    csv_resp = await client.get("/admin/export-csv", cookies=dict(login_resp.cookies))
    assert csv_resp.status_code == 200
    assert "text/csv" in csv_resp.headers["content-type"]
    assert "Full Name" in csv_resp.text


async def test_admin_logout(client):
    """GET /admin/logout should clear cookie and redirect to /admin/login."""
    response = await client.get("/admin/logout", follow_redirects=False)
    assert response.status_code == 303
    assert "/admin/login" in response.headers["location"]
