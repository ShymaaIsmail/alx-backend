#!/usr/bin/env python3
"""a-app.py"""


from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    """Task 0"""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)
