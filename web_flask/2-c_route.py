#!/usr/bin/python3
""" Starts a simple Flask web app.
    The app listens on 0.0.0.0, port 5000.
    Routes:
        /: Displays 'Hello HBNB!'
        /hbnb: Displays 'HBNB'
        /c/<text>: Displays 'C <text>'
"""
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello(strict_slashes=False):
    """Displays 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route('/hbnb')
def hello_bnb(strict_slashes=False):
    """Displays 'HBNB'"""
    return "HBNB"


@app.route('/c/<text>')
def hello_text(strict_slashes=False):
    """ Displays 'C ' followed by <text>"""
    texter = text.replace("_", " ")
    return "C {}".format(texter)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
