#!/usr/bin/python3
""" Starts a simple Flask web app.
    The app listens on 0.0.0.0, port 5000.
    Routes:
        /: Displays 'Hello HBNB!'
        /hbnb: Displays 'HBNB'
        /c/<text>: Displays 'C <text>'
        /python/(<text>): Displays 'Python <text>'
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Displays 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hello_hbnb():
    """Displays 'HBNB'"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def hello_c(text, strict_slashes=False):
    """ Displays 'C ' followed by <text>"""
    return "C {}".format(text.replace('_', ' '))


@app.route("/python", strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def hello_python(text='is cool'):
    """ Displays 'Python ' followed by <text>"""
    return "Python {}".format(text.replace('_', ' '))


if __name__ == "__main__":
    app.run(host="0.0.0.0")
