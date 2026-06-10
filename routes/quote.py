from flask import Blueprint
from flask import jsonify
import sqlite3
import random

quotes_bp = Blueprint(
    "quotes",
    __name__
)

@quotes_bp.route("/api/quotes")
def get_quotes():

    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row

    data = conn.execute(
        "SELECT * FROM quotes"
    ).fetchall()

    conn.close()

    return jsonify(
        [dict(row) for row in data]
    )

@quotes_bp.route("/api/quotes/random")
def random_quote():

    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row

    data = conn.execute(
        "SELECT * FROM quotes"
    ).fetchall()

    conn.close()

    return jsonify(
        dict(random.choice(data))
    )