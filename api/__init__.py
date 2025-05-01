from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from datetime import timedelta
import os

db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)

    # ── Config ──────────────────────────────────────────────────────────────
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL", "sqlite:///sage.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET", "dev-secret-change-me")
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=15)
    app.config["JWT_TOKEN_LOCATION"] = ["cookies"]
    app.config["JWT_COOKIE_CSRF_PROTECT"] = False  # SPA handles CSRF separately

    # ── Extensions ──────────────────────────────────────────────────────────
    db.init_app(app)
    jwt.init_app(app)
    CORS(app, supports_credentials=True, origins=[
        "http://localhost:5173",
    ])

    # ── Blueprints ──────────────────────────────────────────────────────────
    from .auth.routes import auth_bp
    from .suggestions.routes import sugg_bp

    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(sugg_bp, url_prefix="/")

    @app.route("/health")
    def health():
        return {"status": "ok"}, 200

    return app
