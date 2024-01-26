#!/usr/bin/python3
"""Starts a Flask web application.
The application listens on 0.0.0.0, port 5000
"""
from flask import Flask, render_template

app = Flask("__name__")


@app.route('/', strict_slashes=False)
def hello():
    """Returns given string"""
    return render_template("10-hbnb_filters.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
