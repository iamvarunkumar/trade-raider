from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, set_access_cookies, unset_jwt_cookies
from .. import db
from ..models import User
from pydantic import BaseModel, EmailStr, ValidationError

auth_bp = Blueprint("auth", __name__)

# ── Schemas ────────────────────────────────────────────────────────────────
class RegisterBody(BaseModel):
    email: EmailStr
    password: str

class LoginBody(RegisterBody): ...


# ── Routes ────────────────────────────────────────────────────────────────
@auth_bp.post("/register")
def register():
    try:
        body = RegisterBody(**request.json)
    except ValidationError as err:
        return err.json(), 400

    if User.query.filter_by(email=body.email).first():
        return jsonify({"msg": "Email already registered"}), 409

    user = User(email=body.email, password_h=User.hash_pw(body.password))
    db.session.add(user)
    db.session.commit()
    return jsonify({"id": user.id}), 201


@auth_bp.post("/login")
def login():
    try:
        body = LoginBody(**request.json)
    except ValidationError as err:
        return err.json(), 400

    user = User.query.filter_by(email=body.email).first()
    if not user or not user.verify_pw(body.password):
        return jsonify({"msg": "Bad credentials"}), 401

    access = create_access_token(identity=user.id)
    resp = jsonify({"msg": "login ok"})
    set_access_cookies(resp, access)
    return resp, 200


@auth_bp.post("/logout")
def logout():
    resp = jsonify({"msg": "logout"})
    unset_jwt_cookies(resp)
    return resp, 200
