"""
Tests for main pages and static routes.
"""

import pytest
from httpx import ASGITransport, AsyncClient

from app.main import app

pytestmark = pytest.mark.asyncio


async def test_homepage_returns_200(client):
    """GET / should return a 200 status code."""
    response = await client.get("/")
    assert response.status_code == 200


async def test_homepage_contains_brand(client):
    """The homepage should contain the 'Aurocous' brand name."""
    response = await client.get("/")
    assert "Aurocous" in response.text


async def test_homepage_contains_sections(client):
    """The homepage should contain key section headings and not contain Products section."""
    response = await client.get("/")
    html = response.text

    expected_sections = [
        "Technology Built Around Your Business.",
        "Engineering Solutions for Modern Businesses.",
        "A Clear Path from Idea to Implementation.",
        "Technology for Different Business Environments.",
        "Why Businesses Choose Aurocous.",
        "Let's Build Something Meaningful.",
    ]
    for section in expected_sections:
        assert section in html, f"Missing section: {section}"

    # Confirm Product Innovation section and products links are completely removed
    assert "Product Innovation" not in html
    assert 'href="#products"' not in html


async def test_homepage_has_meta_tags(client):
    """The homepage should contain meta description and Open Graph tags."""
    response = await client.get("/")
    html = response.text

    # Meta description
    assert 'name="description"' in html
    assert "Aurocous helps businesses build digital solutions" in html

    # Open Graph tags
    assert 'property="og:title"' in html
    assert 'property="og:description"' in html
    assert 'property="og:image"' in html
    assert 'property="og:url"' in html


async def test_robots_txt(client):
    """GET /robots.txt should return 200 with text/plain content type."""
    response = await client.get("/robots.txt")
    assert response.status_code == 200
    assert "text/plain" in response.headers["content-type"]
    assert "User-agent" in response.text


async def test_sitemap_xml(client):
    """GET /sitemap.xml should return 200 with XML content."""
    response = await client.get("/sitemap.xml")
    assert response.status_code == 200
    content_type = response.headers["content-type"]
    assert "xml" in content_type or "text/xml" in content_type
    assert "<?xml" in response.text
    assert "<urlset" in response.text


async def test_static_files_accessible(client):
    """GET /static/css/style.css should return 200."""
    response = await client.get("/static/css/style.css")
    assert response.status_code == 200
