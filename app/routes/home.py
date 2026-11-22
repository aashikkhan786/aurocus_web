"""Home page route."""

import secrets
from datetime import datetime

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from app.config import settings
from app.templates_config import templates
from app.services.content_service import (
    get_services,
    get_industries,
    get_approach_steps,
    get_reasons,
    get_products,
    get_stats,
    get_countries,
)

router = APIRouter(tags=["pages"])


@router.get("/", response_class=HTMLResponse)
async def home(request: Request, submitted: str | None = None):
    """Render the homepage with all content context."""
    # Generate CSRF token
    csrf_token = secrets.token_hex(32)

    # Check for successful submission
    form_success = True if submitted == "true" else None

    context = {
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
        "form_data": {},
        "form_errors": {},
        "form_success": form_success,
        "current_year": datetime.now().year,
    }

    response = templates.TemplateResponse(
        request=request, name="index.html", context=context
    )

    # Set CSRF token as HttpOnly cookie
    response.set_cookie(
        key="csrf_token",
        value=csrf_token,
        httponly=True,
        samesite="strict",
    )

    return response
