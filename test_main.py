import pytest
from fastapi.testclient import TestClient

from main import add, app

client = TestClient(app)


def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(1, "2") is None


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello from ci_cd_learn"}


def test_add_endpoint():
    response = client.get("/add", params={"a": 1, "b": 2})
    assert response.status_code == 200
    assert response.json() == {"result": 3}
