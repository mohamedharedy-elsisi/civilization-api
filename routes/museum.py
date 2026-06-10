from flask import Blueprint
from flask import jsonify
import json

museums_bp = Blueprint(
    "museums",
    __name__
)

@museums_bp.route("/api/museums")
def get_museums():

    with open(
        "datafiles/museums.json",
        "r",
        encoding="utf-8"
    ) as file:

        data = json.load(file)

    return jsonify(data)