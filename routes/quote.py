from flask import Blueprint
from flask import jsonify
import json
import random

quotes_bp = Blueprint(
    "quotes",
    __name__
)

@quotes_bp.route("/api/quotes")
def get_quotes():

    with open(
        "datafiles/quotes.json",
        "r",
        encoding="utf-8"
    ) as file:

        data = json.load(file)

    return jsonify(data)

@quotes_bp.route("/api/quotes/random")
def random_quote():

    with open(
        "datafiles/quotes.json",
        "r",
        encoding="utf-8"
    ) as file:

        data = json.load(file)

    return jsonify(
        random.choice(data)
    )