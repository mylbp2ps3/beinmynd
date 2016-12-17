from flask import Flask, render_template, send_from_directory
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/datasets/<dataset_file>/")
def datasets(dataset_file):
    return send_from_directory('static', "sample_datasets/" + dataset_file)


if __name__ == "__main__":
    app.run()
