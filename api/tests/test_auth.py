from api import create_app, db
from flask.testing import FlaskClient
import pytest, json, os

@pytest.fixture()
def client():
    app = create_app()
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    with app.app_context():
        db.create_all()
        yield app.test_client()                             # type: FlaskClient

def test_register_and_login(client):
    # register
    res = client.post("/auth/register", json={"email": "foo@bar.com", "password": "P@ssw0rd"})
    assert res.status_code == 201

    # login
    res = client.post("/auth/login", json={"email": "foo@bar.com", "password": "P@ssw0rd"})
    assert res.status_code == 200
    assert "access_token_cookie" in res.headers.getlist("Set-Cookie")[0]
