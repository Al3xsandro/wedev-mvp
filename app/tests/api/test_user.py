from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_auth_with_incorrect_credentials():
    body = {
        "username": "john@gmail.com",
        "password": "teste",
    }

    response = client.post("/auth", data=body)
    assert response.status_code == 400


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

    response = client.post("/users", json=body)
    assert response.status_code == 401
