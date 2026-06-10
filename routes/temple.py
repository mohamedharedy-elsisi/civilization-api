from flask import Blueprint
from flask import jsonify
import json

temples_bp = Blueprint(
    "temples",
    __name__
)

@temples_bp.route("/api/temples")
def get_temples():

    with open(
        "datafiles/temples.json",
        "r",
        encoding="utf-8"
    ) as file:

        data = json.load(file)

    return jsonify(data)