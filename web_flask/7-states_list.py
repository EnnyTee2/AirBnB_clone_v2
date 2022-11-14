#!/usr/bin/python3
""" Starts a simple Flask web app.
    The app listens on 0.0.0.0, port 5000.
    Routes:
        /: Displays 'Hello HBNB!'
        /hbnb: Displays 'HBNB'
        /c/<text>: Displays 'C <text>'
        /python/(<text>): Displays 'Python <text>'
        /number/<n>: display 'n is a number' if n is an integer
"""
from flask import Flask
from flask import render_template
from models import storage


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def list_states():
    states = storage.all('States')
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown():
    """Method to remove current SQLAlchemy session
       after each request
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
