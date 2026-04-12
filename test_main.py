from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


class TestAPI:

    def test_home(self):
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == {"message": "Hello Shakthi!!"}

    def test_greet_default(self):
        response = client.get("/greet")
        assert response.status_code == 200
        assert response.json() == {"message": "Hello, Guest!"}

    def test_greet_with_name(self):
        response = client.get("/greet?name=Shakthi")
        assert response.status_code == 200
        assert response.json() == {"message": "Hello, Shakthi!"}

    def test_add(self):
        response = client.get("/add?a=5&b=3")
        assert response.status_code == 200
        assert response.json()["result"] == 8

    def test_error(self):
        response = client.get("/error")
        assert response.status_code == 400
        assert response.json()["detail"] == "This is a simulated error"

    def test_divide_success(self):
        response = client.get("/divide?a=10&b=2")
        assert response.status_code == 200
        assert response.json()["result"] == 5

    def test_divide_by_zero(self):
        response = client.get("/divide?a=10&b=0")
        assert response.status_code == 400
        assert response.json()["detail"] == "Cannot divide by zero"