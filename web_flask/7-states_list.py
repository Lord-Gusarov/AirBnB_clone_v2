#!/usr/bin/python3
"""Starts a Flask web application
"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardwon(exception=None):
    storage.close()


@app.route('/states_list')
def states_list():
    """Returns list of States in html template"""
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run()
