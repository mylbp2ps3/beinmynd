from flask import Flask, render_template, send_from_directory

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


if __name__ == "__main__":
    app.run() 
