from flask import Blueprint
from flask import jsonify
import json

statues_bp = Blueprint(
    "statues",
    __name__
)

@statues_bp.route("/api/statues")
def get_statues():

    with open(
        "datafiles/statues.json",
        "r",
        encoding="utf-8"
    ) as file:

        data = json.load(file)

    return jsonify(data)