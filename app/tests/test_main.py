from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_send_email():
    response = client.post(
        "api/send_email",
        json={
            "to": "recipient@example.com",
            "subject": "Test email",
            "message": "This is a test email."
        }
    )
    assert response.status_code == 200
    assert response.json() == {"message": "Email sent"}
