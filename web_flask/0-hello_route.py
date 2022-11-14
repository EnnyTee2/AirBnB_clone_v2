#!/usr/bin/env python3

from flask import Flask
app = Flask(__main__)

@app.route('/')
def hello_world(strict_slashes=False):
    return "Hello HBNB!"
