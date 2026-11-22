"""FastAPI application entry point."""

from contextlib import asynccontextmanager
import os

from fastapi import FastAPI, Request, Response
from fastapi.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware

from app.config import settings
from app.database import init_db
from app.routes import home, contact, seo, admin


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Initialize the database on application startup."""
    init_db()
    yield


app = FastAPI(title="Aurocous", debug=settings.DEBUG, lifespan=lifespan)

# --- Static files ---
static_dir = os.path.join(os.path.dirname(__file__), "static")
os.makedirs(static_dir, exist_ok=True)
app.mount("/static", StaticFiles(directory=static_dir), name="static")

# --- CORS middleware ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# --- Security headers middleware ---
@app.middleware("http")
async def add_security_headers(request: Request, call_next):
    """Add security headers to all responses."""
    response: Response = await call_next(request)

    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["X-XSS-Protection"] = "1; mode=block"
    response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
    response.headers["Content-Security-Policy"] = (
        "default-src 'self'; "
        "script-src 'self' 'unsafe-inline'; "
        "style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; "
        "font-src 'self' https://fonts.gstatic.com; "
        "img-src 'self' data:; "
        "connect-src 'self';"
    )

    # Static file caching
    if request.url.path.startswith("/static"):
        response.headers["Cache-Control"] = "public, max-age=31536000, immutable"

    return response


# --- Include routers ---
app.include_router(home.router)
app.include_router(contact.router)
app.include_router(seo.router)
app.include_router(admin.router)



