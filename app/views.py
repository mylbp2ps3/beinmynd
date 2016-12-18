from app import app
from flask import render_template, send_from_directory

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/datasets/<dataset_file>/")
def datasets(dataset_file):
    return send_from_directory('static', "sample_datasets/" + dataset_file)