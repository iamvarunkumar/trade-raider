from api import create_app, db
from flask.testing import FlaskClient
import pytest, json

@pytest.fixture()
def authed_client():
    app = create_app()
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    with app.app_context():
        db.create_all()
        c = app.test_client()
        c.post("/auth/register", json={"email": "u@x.com", "password": "abc12345"})
        c.post("/auth/login", json={"email": "u@x.com", "password": "abc12345"})
        yield c                                            # type: FlaskClient

def test_suggestions(authed_client):
    res = authed_client.get("/suggestions")
    assert res.status_code == 200
    data = res.get_json()
    assert len(data) == 40
