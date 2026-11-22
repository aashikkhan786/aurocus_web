"""SEO routes — robots.txt and sitemap.xml."""

from datetime import datetime

from fastapi import APIRouter
from fastapi.responses import PlainTextResponse, Response

from app.config import settings

router = APIRouter()


@router.get("/robots.txt", response_class=PlainTextResponse)
async def robots_txt():
    """Serve robots.txt for search engine crawlers."""
    content = (
        "User-agent: *\n"
        "Allow: /\n"
        "\n"
        f"Sitemap: {settings.SITE_URL}/sitemap.xml\n"
    )
    return PlainTextResponse(content=content)


@router.get("/sitemap.xml")
async def sitemap_xml():
    """Serve sitemap.xml for search engine indexing."""
    today = datetime.now().strftime("%Y-%m-%d")
    xml_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url>
        <loc>{settings.SITE_URL}/</loc>
        <lastmod>{today}</lastmod>
        <changefreq>weekly</changefreq>
        <priority>1.0</priority>
    </url>
</urlset>"""
    return Response(content=xml_content, media_type="application/xml")
