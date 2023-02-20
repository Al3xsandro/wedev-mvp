import pytest
from fastapi.testclient import TestClient
from typing import Generator

from typing import Dict

from app.main import app
from app.database.database import SessionLocal

from app.tests.utils.utils import create_staff_user


@pytest.fixture(scope="session")
def db() -> Generator:
    yield SessionLocal()


@pytest.fixture(scope="session")
async def client() -> Generator:
    with TestClient(app) as c:
        yield c


@pytest.fixture(scope="module")
def create_staff(client: TestClient) -> Dict[str, str]:
    return create_staff_user(client)
