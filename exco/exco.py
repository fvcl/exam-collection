import flask
from flask import render_template, request, redirect, url_for

app = flask.Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
