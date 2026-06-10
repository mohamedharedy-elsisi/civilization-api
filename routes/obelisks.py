from flask import Blueprint
from flask import jsonify
from flask import request

import sqlite3
import json

obelisks_bp = Blueprint(
    "obelisks",
    __name__
)


@obelisks_bp.route("/api/obelisks")
def get_obelisks():

    conn = sqlite3.connect(
        "database.db"
    )

    conn.row_factory = sqlite3.Row

    data = conn.execute(
        "SELECT * FROM obelisks"
    ).fetchall()

    conn.close()

    result = []

    for row in data:

        item = dict(row)

        item["images"] = json.loads(
            item["images"]
        )

        result.append(item)

    return jsonify(result)


@obelisks_bp.route("/api/obelisks/<int:id>")
def get_obelisk(id):

    conn = sqlite3.connect(
        "database.db"
    )

    conn.row_factory = sqlite3.Row

    row = conn.execute(
        "SELECT * FROM obelisks WHERE id = ?",
        (id,)
    ).fetchone()

    conn.close()

    if row is None:

        return jsonify({
            "message": "Obelisk not found"
        }), 404

    item = dict(row)

    item["images"] = json.loads(
        item["images"]
    )

    return jsonify(item)


@obelisks_bp.route("/api/obelisks/search")
def search_obelisks():

    query = request.args.get(
        "q",
        ""
    )

    conn = sqlite3.connect(
        "database.db"
    )

    conn.row_factory = sqlite3.Row

    data = conn.execute("""
        SELECT *
        FROM obelisks
        WHERE
        name LIKE ?
        OR arabic_name LIKE ?
        OR city LIKE ?
        OR builder LIKE ?
        OR historical_era LIKE ?
    """, (
        f"%{query}%",
        f"%{query}%",
        f"%{query}%",
        f"%{query}%",
        f"%{query}%"
    )).fetchall()

    conn.close()

    result = []

    for row in data:

        item = dict(row)

        item["images"] = json.loads(
            item["images"]
        )

        result.append(item)

    return jsonify(result)