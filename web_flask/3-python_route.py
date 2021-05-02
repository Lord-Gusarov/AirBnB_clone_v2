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


@app.route('/c/<text>')
def hello_c(text):
    """Greets C stuff
    """
    return ("C {}".format(text.replace('_', ' ')))


@app.route('/python')
@app.route('/python/<text>')
def hello_python(text='is cool'):
    """Greets Python stuff
    """
    return ("Python {}".format(text.replace('_', ' ')))


if __name__ == '__main__':
    app.run()
