from flask import Blueprint
from flask import jsonify
import sqlite3

temples_bp = Blueprint(
    "temples",
    __name__
)

@temples_bp.route("/api/temples")
def get_temples():

    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row

    data = conn.execute(
        "SELECT * FROM temples"
    ).fetchall()

    conn.close()

    return jsonify(
        [dict(row) for row in data]
    )