#!/usr/bin/env python3
# Purpose: Top level API for for Tree View
# Usage:
#    source venv/bin/activate
#    export FLASK_ENV=development ; FLASK_APP=api.py flask run --host=0.0.0.0

import os
from flask import Flask, flash, request, redirect, url_for
from pathlib import Path
from werkzeug.utils import secure_filename

import config

# Config
logger = config.get_logger()
app = Flask(__name__)

# Constants
output_path = Path('./tmp')
allowed_extensions = set(['csv'])


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in allowed_extensions


@app.route("/", methods=['GET'])
def doc_root():
    return '''<!doctype html>
    <title>Tree View</title>
    <h1>Upload building data</h1>
    <form method="POST" action="/buildings/" enctype="multipart/form-data">
      <input type="file" name="file">
      <input type="submit" value="Upload">
    </form>'''


# File upload source: http://flask.pocoo.org/docs/1.0/patterns/fileuploads/
@app.route("/buildings/", methods=['POST'])
def store_building():
    if 'file' not in request.files:
        message = 'No file part'
        logger.error(message)
        flash(message)
        return redirect(request.url)
    file = request.files['file']
    # if user does not select file, browser also
    # submit an empty part without filename
    if file.filename == '':
        message = 'No selected file'
        logger.error(message)
        flash(message)
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(str(output_path), filename))
        return redirect('/')


@app.route("/buildings/", methods=['GET'])
def get_buildings_list():
    return "{}".format(os.listdir(str(output_path)))


@app.route("/buildings/<string:building_id>", methods=['GET'])
def get_building(building_id):
    return "This building is {}".format(building_id)


@app.route("/datasets/update", methods=['POST'])
def update_datasets():
    return "The dataset were updated"
