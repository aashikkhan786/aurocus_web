"""Admin dashboard routes."""

import csv
import hashlib
import hmac
import io
from fastapi import APIRouter, Form, Request, Response
from fastapi.responses import HTMLResponse, RedirectResponse, StreamingResponse

from app.config import settings
from app.database import get_db_connection, close_db
from app.templates_config import templates

router = APIRouter(prefix="/admin", tags=["admin"])

COOKIE_NAME = "aurocous_admin_session"


def _generate_session_token() -> str:
    """Generate a cryptographic session token based on SECRET_KEY and username."""
    return hmac.new(
        settings.SECRET_KEY.encode(),
        settings.ADMIN_USERNAME.encode(),
        hashlib.sha256,
    ).hexdigest()


def _is_authenticated(request: Request) -> bool:
    """Check if the admin session cookie is valid."""
    session = request.cookies.get(COOKIE_NAME)
    if not session:
        return False
    expected = _generate_session_token()
    return hmac.compare_digest(session, expected)


@router.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    """Render the admin login page."""
    if _is_authenticated(request):
        return RedirectResponse(url="/admin", status_code=303)
    return templates.TemplateResponse(
        request=request,
        name="admin/login.html",
        context={"error": None},
    )


@router.post("/login", response_class=HTMLResponse)
async def handle_login(
    request: Request,
    username: str = Form(...),
    password: str = Form(...),
):
    """Validate admin credentials and set session cookie."""
    if (
        hmac.compare_digest(username.strip(), settings.ADMIN_USERNAME)
        and hmac.compare_digest(password.strip(), settings.ADMIN_PASSWORD)
    ):
        response = RedirectResponse(url="/admin", status_code=303)
        response.set_cookie(
            key=COOKIE_NAME,
            value=_generate_session_token(),
            httponly=True,
            samesite="lax",
        )
        return response

    return templates.TemplateResponse(
        request=request,
        name="admin/login.html",
        context={"error": "Invalid username or password. Please try again."},
        status_code=401,
    )


@router.get("/logout")
async def logout():
    """Clear session cookie and redirect to login."""
    response = RedirectResponse(url="/admin/login", status_code=303)
    response.delete_cookie(COOKIE_NAME)
    return response


@router.get("", response_class=HTMLResponse)
@router.get("/", response_class=HTMLResponse)
async def dashboard(request: Request):
    """Display the admin inquiries dashboard."""
    if not _is_authenticated(request):
        return RedirectResponse(url="/admin/login", status_code=303)

    conn = get_db_connection()
    try:
        cursor = conn.execute(
            """
            SELECT id, full_name, business_email, company_name, country,
                   service_interested, project_details, ip_address, created_at
            FROM contact_inquiries
            ORDER BY id DESC
            """
        )
        inquiries = [dict(row) for row in cursor.fetchall()]
    finally:
        close_db(conn)

    # Compute metrics
    total_leads = len(inquiries)
    unique_companies = len({inq["company_name"].lower() for inq in inquiries if inq.get("company_name")})
    services_count = len({inq["service_interested"] for inq in inquiries if inq.get("service_interested")})

    return templates.TemplateResponse(
        request=request,
        name="admin/dashboard.html",
        context={
            "inquiries": inquiries,
            "total_leads": total_leads,
            "unique_companies": unique_companies,
            "services_count": services_count,
            "admin_user": settings.ADMIN_USERNAME,
        },
    )


@router.post("/inquiries/{inquiry_id}/delete")
async def delete_inquiry(request: Request, inquiry_id: int):
    """Delete a contact inquiry."""
    if not _is_authenticated(request):
        return RedirectResponse(url="/admin/login", status_code=303)

    conn = get_db_connection()
    try:
        conn.execute("DELETE FROM contact_inquiries WHERE id = ?", (inquiry_id,))
        conn.commit()
    finally:
        close_db(conn)

    return RedirectResponse(url="/admin", status_code=303)


@router.get("/export-csv")
async def export_csv(request: Request):
    """Export inquiries as a CSV download."""
    if not _is_authenticated(request):
        return RedirectResponse(url="/admin/login", status_code=303)

    conn = get_db_connection()
    try:
        cursor = conn.execute(
            """
            SELECT id, full_name, business_email, company_name, country,
                   service_interested, project_details, ip_address, created_at
            FROM contact_inquiries
            ORDER BY id DESC
            """
        )
        inquiries = cursor.fetchall()
    finally:
        close_db(conn)

    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow([
        "ID", "Full Name", "Business Email", "Company Name",
        "Country", "Service Interested", "Project Details", "IP Address", "Created At"
    ])
    for row in inquiries:
        writer.writerow(list(row))

    output.seek(0)
    return StreamingResponse(
        io.BytesIO(output.getvalue().encode("utf-8-sig")),
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=aurocous_inquiries.csv"},
    )
