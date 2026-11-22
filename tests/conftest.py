"""
Test fixtures and configuration for Aurocous test suite.
"""

import os
import tempfile

import pytest
from httpx import ASGITransport, AsyncClient

# Set test environment variables before importing the app
TEST_DB_FILE = os.path.join(tempfile.gettempdir(), "test_aurocous.db")
os.environ["DATABASE_URL"] = TEST_DB_FILE
os.environ["SECRET_KEY"] = "test-secret-key-for-testing-only"
os.environ["SITE_URL"] = "http://testserver"
os.environ["DEBUG"] = "true"

from app.main import app  # noqa: E402
from app.database import init_db, get_db_path  # noqa: E402


@pytest.fixture(scope="session", autouse=True)
def _initialize_test_database():
    """Initialize the database schema once for the entire test session."""
    # Ensure any previous test file is removed
    if os.path.exists(TEST_DB_FILE):
        try:
            os.remove(TEST_DB_FILE)
        except OSError:
            pass
    init_db()
    yield
    if os.path.exists(TEST_DB_FILE):
        try:
            os.remove(TEST_DB_FILE)
        except OSError:
            pass


@pytest.fixture()
async def client():
    """Provide an async test client for the FastAPI app."""
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://testserver") as c:
        yield c
