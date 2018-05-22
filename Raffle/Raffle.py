from flask import Flask, flash, redirect, render_template, request, session, abort
from random import randint
import random

app = Flask(__name__)

@app.route("/")
def index():
    return "Flask App!"

# @app.route("/hello/<string:name>")
@app.route("/hello/<string:name>/")
def hello(name):
    #    return name
    lines = open("names.txt").readlines()
    quote = random.choice(lines)
    f = open("names.txt", "w")
    for line in lines:
        if line != quote:
            f.write(line)

    return render_template(
        'test.html', **locals())


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)