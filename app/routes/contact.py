"""Contact form route."""

import logging
from datetime import datetime

from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse

from app.config import settings
from app.templates_config import templates
from app.services.contact_service import validate_contact_form, save_inquiry
from app.services.content_service import (
    get_services,
    get_industries,
    get_approach_steps,
    get_reasons,
    get_products,
    get_stats,
    get_countries,
)

logger = logging.getLogger(__name__)

router = APIRouter(tags=["contact"])


def _build_template_context(
    request: Request,
    csrf_token: str,
    form_data: dict | None = None,
    form_errors: dict | None = None,
    form_success: bool | None = None,
) -> dict:
    """Build the full template context for re-rendering index.html."""
    return {
        "request": request,
        "title": "Aurocous | Custom Software & Digital Engineering Solutions",
        "meta_description": "Aurocous helps businesses build digital solutions through web and mobile development, custom software, AI, cloud, UI/UX, and data engineering.",
        "canonical_url": settings.SITE_URL,
        "og_image": f"{settings.SITE_URL}/static/images/og-image.png",
        "services": get_services(),
        "industries": get_industries(),
        "approach_steps": get_approach_steps(),
        "reasons": get_reasons(),
        "products": get_products(),
        "stats": get_stats(),
        "countries": get_countries(),
        "csrf_token": csrf_token,
        "form_data": form_data or {},
        "form_errors": form_errors or {},
        "form_success": form_success,
        "current_year": datetime.now().year,
    }


@router.post("/contact")
async def handle_contact(request: Request):
    """Handle contact form submission."""
    form = await request.form()
    form_data = dict(form)

    # Get CSRF tokens
    form_csrf = form_data.get("csrf_token", "")
    cookie_csrf = request.cookies.get("csrf_token", "")

    # Validate CSRF token
    if not form_csrf or not cookie_csrf or form_csrf != cookie_csrf:
        logger.warning("CSRF token mismatch from IP: %s", request.client.host if request.client else "unknown")
        context = _build_template_context(
            request=request,
            csrf_token=cookie_csrf,
            form_data=form_data,
            form_errors={"_form": "Security validation failed. Please try again."},
        )
        return templates.TemplateResponse(
            request=request, name="index.html", context=context, status_code=403
        )

    # Check honeypot field
    honeypot = form_data.get("_honeypot", "")
    if honeypot:
        # Silently reject bot submission without showing success
        return RedirectResponse(url="/", status_code=303)

    # Validate form fields
    form_errors = validate_contact_form(form_data)

    if form_errors:
        context = _build_template_context(
            request=request,
            csrf_token=cookie_csrf,
            form_data=form_data,
            form_errors=form_errors,
        )
        return templates.TemplateResponse(
            request=request, name="index.html", context=context, status_code=200
        )

    # Save to database
    try:
        ip_address = request.client.host if request.client else "unknown"
        user_agent = request.headers.get("user-agent", "unknown")

        inquiry_id = save_inquiry(
            data=form_data,
            ip_address=ip_address,
            user_agent=user_agent,
        )
        logger.info("Contact inquiry saved with ID: %d", inquiry_id)
    except Exception:
        logger.exception("Failed to save contact inquiry")
        context = _build_template_context(
            request=request,
            csrf_token=cookie_csrf,
            form_data=form_data,
            form_errors={"_form": "An error occurred while processing your request. Please try again later."},
        )
        return templates.TemplateResponse(
            request=request, name="index.html", context=context, status_code=500
        )

    return RedirectResponse(url="/?submitted=true", status_code=303)
