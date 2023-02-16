import pytest
from fastapi.testclient import TestClient

from typing import Generator


from app.main import app
from app.database.database import SessionLocal


@pytest.fixture(scope="function")
async def client() -> Generator:
    with TestClient(app) as c:
        yield c


@pytest.fixture(scope="session")
def db() -> Generator:
    yield SessionLocal()
