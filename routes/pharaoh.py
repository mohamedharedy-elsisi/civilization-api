from flask import Blueprint
from flask import jsonify
import json

pharaohs_bp = Blueprint(
    "pharaohs",
    __name__
)

@pharaohs_bp.route("/api/pharaohs")
def get_pharaohs():

    with open(
        "datafiles/pharaohs.json",
        "r",
        encoding="utf-8"
    ) as file:

        data = json.load(file)

    return jsonify(data)