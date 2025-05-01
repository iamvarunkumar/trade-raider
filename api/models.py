from . import db
from passlib.hash import bcrypt
from datetime import datetime
from decimal import Decimal, ROUND_HALF_UP

class User(db.Model):
    __tablename__ = "users"
    id          = db.Column(db.Integer, primary_key=True)
    email       = db.Column(db.String(255), unique=True, nullable=False)
    password_h  = db.Column(db.String(255), nullable=False)
    created_at  = db.Column(db.DateTime, default=datetime.utcnow)

    # ── Helpers ────────────────────────────────────────────────────────────
    @staticmethod
    def hash_pw(raw: str) -> str:
        return bcrypt.hash(raw, rounds=12)

    def verify_pw(self, raw: str) -> bool:
        return bcrypt.verify(raw, self.password_h)

DEC = lambda x: Decimal(str(x)).quantize(Decimal("0.01"), ROUND_HALF_UP)

class Trade(db.Model):
    __tablename__ = "paper_trades"
    id         = db.Column(db.Integer, primary_key=True)
    user_id    = db.Column(db.Integer, db.ForeignKey("users.id"))
    ticker     = db.Column(db.String(10))
    side       = db.Column(db.Enum("buy", "sell", name="trade_side"))
    qty        = db.Column(db.Integer)
    price      = db.Column(db.Float)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Snapshot(db.Model):
    __tablename__ = "portfolio_snapshots"
    id          = db.Column(db.Integer, primary_key=True)
    user_id     = db.Column(db.Integer)
    equity_val  = db.Column(db.Float)  # total market value
    cash        = db.Column(db.Float)
    pnl         = db.Column(db.Float)  # cumulative P/L %
    created_at  = db.Column(db.DateTime, default=datetime.utcnow)
