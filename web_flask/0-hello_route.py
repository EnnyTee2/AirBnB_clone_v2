#!/usr/bin/python3
""" Starts a simple Flask web app.
    The app listens on 0.0.0.0, port 5000.
    Routes:
        /: Displays 'Hello HBNB!'
"""
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello(strict_slashes=False):
    """Displays 'Hello HBNB!'"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
