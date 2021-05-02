#!/usr/bin/python3
"""Starts a Flask web application
"""
from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    """Greets
    """
    return ('Hello HBNB!')


@app.route('/hbnb')
def hello_hbnb():
    """Greets HBNB
    """
    return ('HBNB')


if __name__ == '__main__':
    app.run()
