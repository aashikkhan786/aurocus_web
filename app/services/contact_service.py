"""Contact form service — validation and persistence."""

import re
from app.database import get_db_connection, close_db


def validate_contact_form(form_data: dict) -> dict:
    """Validate contact form data and return a dict of field_name -> error_message.

    Returns an empty dict if all fields are valid.
    """
    errors: dict[str, str] = {}

    # Full name
    full_name = (form_data.get("full_name") or "").strip()
    if not full_name:
        errors["full_name"] = "Full name is required."
    elif len(full_name) < 2:
        errors["full_name"] = "Full name must be at least 2 characters."

    # Business email
    business_email = (form_data.get("business_email") or "").strip()
    if not business_email:
        errors["business_email"] = "Business email is required."
    else:
        email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if not re.match(email_pattern, business_email):
            errors["business_email"] = "Please enter a valid email address."

    # Company name
    company_name = (form_data.get("company_name") or "").strip()
    if not company_name:
        errors["company_name"] = "Company name is required."
    elif len(company_name) < 2:
        errors["company_name"] = "Company name must be at least 2 characters."

    # Country
    country = (form_data.get("country") or "").strip()
    if not country:
        errors["country"] = "Please select a country."

    # Service interested
    service_interested = (form_data.get("service_interested") or "").strip()
    if not service_interested:
        errors["service_interested"] = "Please select a service."

    # Project details
    project_details = (form_data.get("project_details") or "").strip()
    if not project_details:
        errors["project_details"] = "Project details are required."
    elif len(project_details) < 10:
        errors["project_details"] = "Project details must be at least 10 characters."

    return errors


def save_inquiry(data: dict, ip_address: str, user_agent: str) -> int:
    """Save a contact inquiry to the database.

    Args:
        data: Validated form data dict.
        ip_address: Client IP address.
        user_agent: Client User-Agent string.

    Returns:
        The ID of the newly created inquiry.

    Raises:
        Exception: If the database operation fails.
    """
    conn = get_db_connection()
    try:
        cursor = conn.execute(
            """
            INSERT INTO contact_inquiries
                (full_name, business_email, company_name, country,
                 service_interested, project_details, ip_address, user_agent)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                data["full_name"].strip(),
                data["business_email"].strip(),
                data["company_name"].strip(),
                data["country"].strip(),
                data["service_interested"].strip(),
                data["project_details"].strip(),
                ip_address,
                user_agent,
            ),
        )
        conn.commit()
        return cursor.lastrowid
    except Exception:
        conn.rollback()
        raise
    finally:
        close_db(conn)
