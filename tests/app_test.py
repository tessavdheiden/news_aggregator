from starlette.testclient import TestClient

from application import app

client = TestClient(app)

def test_pages():
    response = client.get("/search")
    assert response.status_code == 200
    response = client.get("/sources")
    assert response.status_code == 200