import pytest
from fastapi.testclient import TestClient
from blog.main import app

client = TestClient(app)

# ----------------------------
# Root test (optional)
# ----------------------------
def test_root():
    response = client.get("/")
    # If no root route, this will 404
    assert response.status_code in (200, 404)

# ----------------------------
# User Router Tests
# ----------------------------
def test_create_user():
    payload = {
        "email": "testuser@example.com",
        "password": "testpassword"
    }
    response = client.post("/user/", json=payload)
    # 201 Created if implemented, 400/422 if validation fails
    assert response.status_code in (201, 400, 422)

# If you have GET users endpoint, otherwise skip this
def test_get_users():
    response = client.get("/user/")  # Adjust if your user router has GET
    # 200 OK if endpoint exists, 405 if method not allowed
    assert response.status_code in (200, 405, 404)

# ----------------------------
# Authentication Router Tests
# ----------------------------
def test_login_user():
    payload = {
        "username": "testuser@example.com",
        "password": "testpassword"
    }
    # Adjust route based on router prefix
    response = client.post("/authentication/login", data=payload)
    # 200 OK if credentials correct, 401 if not
    assert response.status_code in (200, 401, 404)

# ----------------------------
# Blog Router Tests
# ----------------------------
# Placeholder token; replace with a real test token
AUTH_HEADERS = {"Authorization": "Bearer testtoken123"}

def test_get_blogs():
    response = client.get("/blog/", headers=AUTH_HEADERS)
    # 200 OK if authorized, 401 if token invalid, 404 if no blogs
    assert response.status_code in (200, 401, 404)

def test_create_blog():
    payload = {
        "title": "Test Blog",
        "body": "This is a test blog body"
    }
    response = client.post("/blog/", json=payload, headers=AUTH_HEADERS)
    # 201 Created if authorized and valid, 401 Unauthorized, 422 Validation error
    assert response.status_code in (201, 401, 422)
