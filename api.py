#!/usr/bin/env python3
# Purpose: Top level API for for Tree View
# Usage:
#    source venv/bin/activate
#    export FLASK_ENV=development ; FLASK_APP=api.py flask run --host=0.0.0.0

from flask import Flask

import config

# Config
logger = config.get_logger()
app = Flask(__name__)

# Constants
output_path = './tmp'


@app.route("/", methods=['GET'])
def hello():
    return "This is the doc root that will serve the HTML site page"


@app.route("/buildings/", methods=['POST'])
def store_building():
    return "Some updated buildings"


@app.route("/buildings/", methods=['GET'])
def get_buildings_list():
    return "Some buildings"


@app.route("/buildings/<string:building_id>", methods=['GET'])
def get_building(building_id):
    return "This building is {}".format(building_id)


@app.route("/datasets/update", methods=['POST'])
def update_datasets():
    return "The dataset were updated"
