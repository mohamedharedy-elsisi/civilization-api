from flask import Blueprint
from flask import jsonify
import sqlite3
import json

pharaohs_bp = Blueprint(
    "pharaohs",
    __name__
)

@pharaohs_bp.route("/api/pharaohs")
def get_pharaohs():

    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row

    data = conn.execute(
        "SELECT * FROM pharaohs"
    ).fetchall()

    conn.close()

    result = []

    for row in data:

        item = dict(row)

        item["achievements"] = json.loads(
            item["achievements"]
        )

        result.append(item)

    return jsonify(result)