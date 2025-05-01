from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required
import time

sugg_bp = Blueprint("suggestions", __name__)

_SAMPLE = {
    "momentum": ["NVDA", "TSLA", "AMD", "META", "NFLX",
                 "SHOP", "UBER", "ABNB", "PLTR", "CRM"],
    "growth":   ["SNOW", "CRWD", "DDOG", "MDB", "SQ",
                 "COIN", "SMCI", "ZS", "NET", "PINS"],
    "value":    ["MSFT", "AAPL", "GOOGL", "BRK.B", "JNJ",
                 "PG", "V", "HD", "KO", "PEP"],
    "watch":    ["ARM", "RIVN", "AI", "FSLY", "SOFI",
                 "DKNG", "ROKU", "LYFT", "RBLX", "COUR"]
}

@sugg_bp.get("/suggestions")
@jwt_required()
def suggestions():
    time.sleep(0.2)       # simulate latency
    payload = [
        {"symbol": s, "category": cat}
        for cat, syms in _SAMPLE.items()
        for s in syms
    ]
    return jsonify(payload), 200
