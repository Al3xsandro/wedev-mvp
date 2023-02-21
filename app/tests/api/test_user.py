from fastapi.testclient import TestClient
from app.main import app
from app.tests.utils.utils import random_email, random_lower_string

from app.core.settings import DEFAULT_USER, DEFAULT_PASSWORD

client = TestClient(app)


def test_auth_with_incorrect_credentials():
    body = {
        "username": "john@gmail.com",
        "password": "teste",
    }

    response = client.post("/session/auth", data=body)
    assert response.status_code == 400


def test_auth_with_staff_credentials(create_staff):
    body = {
        "username": DEFAULT_USER,
        "password": DEFAULT_PASSWORD,
    }

    response = client.post("/session/auth", data=body)
    response_data = response.json()

    assert response.status_code == 200
    assert response_data["access_token"]


def test_create_user_without_staff_role():
    body = {
        "firstName": "John",
        "lastName": "Leao",
        "email": "john@gmail.com",
        "password": "teste",
        "role": "STUDENT",
        "state": "SP",
        "city": "SP",
        "address": "Rua José Pereira Fontes",
        "postalCode": "00000-000",
    }

    response = client.post("/users", data=body)
    assert response.status_code == 401


def test_create_user_with_staff_role():
    body = {
        "firstName": "John",
        "lastName": "Leao",
        "email": f"{random_email}",
        "password": f"{random_lower_string}",
        "role": "STUDENT",
        "state": "SP",
        "city": "SP",
        "address": "Rua José Pereira Fontes",
        "postalCode": "00000-000",
    }

    response = client.post("/users", data=body)
    assert response.status_code == 401
