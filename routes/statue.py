from flask import Blueprint
from flask import jsonify
import sqlite3

statues_bp = Blueprint(
    "statues",
    __name__
)

@statues_bp.route("/api/statues")
def get_statues():

    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row

    data = conn.execute(
        "SELECT * FROM statues"
    ).fetchall()

    conn.close()

    return jsonify(
        [dict(row) for row in data]
    )