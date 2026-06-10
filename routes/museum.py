from flask import Blueprint
from flask import jsonify
import sqlite3

museums_bp = Blueprint(
    "museums",
    __name__
)

@museums_bp.route("/api/museums")
def get_museums():

    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row

    data = conn.execute(
        "SELECT * FROM museums"
    ).fetchall()

    conn.close()

    return jsonify(
        [dict(row) for row in data]
    )