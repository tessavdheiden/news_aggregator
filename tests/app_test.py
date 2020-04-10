from starlette.testclient import TestClient

from application import app

client = TestClient(app)

def test_pages():
    response = client.get("/pages")
    assert response.status_code == 200