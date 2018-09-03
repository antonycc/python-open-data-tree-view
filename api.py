#!/usr/bin/env python3
# Purpose: Top level API for for Tree View
# Usage:
#    source venv/bin/activate
#    export FLASK_ENV=development ; FLASK_APP=api.py flask run --host=0.0.0.0

import os

from flask import Flask, request, redirect, jsonify
from pathlib import Path
from werkzeug.utils import secure_filename
import pandas as pd

import config
import persistence
from api_error import ClientError, ServerError

# Config
logger = config.get_logger()
app = Flask(__name__)

# Constants
output_path = Path('./tmp')


@app.route('/', methods=['GET'])
def root():
    return app.send_static_file('index.html')


@app.route('/main.js', methods=['GET'])
def main():
    return app.send_static_file('main.js')


# File upload source: http://flask.pocoo.org/docs/1.0/patterns/fileuploads/
@app.route('/buildings/', methods=['POST'])
def store_building():
    if not persistence.populated_file(request, 'file'):
        raise ClientError('file is a mandatory POST body element', status_code=400)
    file = request.files['file']
    if not persistence.allowed_file(file.filename):
        raise ClientError('Extension not supported, use: {}'.format(persistence.allowed_extensions), status_code=400)
    filename = secure_filename(file.filename)
    file.save(os.path.join(str(output_path), filename))
    return redirect('/')


@app.route('/buildings/', methods=['GET'])
def get_buildings_list():
    buildings = [(persistence.sha3(b), b) for b in os.listdir(str(output_path))]
    return jsonify(buildings)


@app.route('/buildings/<string:building_id>', methods=['GET'])
def get_building(building_id):
    for building in os.listdir(str(output_path)):
        if persistence.sha3(building) == building_id:
            building_filepath = os.path.join(str(output_path), building)
            df = pd.read_csv(filepath_or_buffer=str(building_filepath))
            return jsonify(df.to_dict())
    raise ClientError('building id is not known: '.format(building_id), status_code=404)


@app.route('/datasets/update', methods=['POST'])
def update_datasets():
    return ServerError('Dataset update is not implemented', status_code=501)


@app.errorhandler(ClientError)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response
