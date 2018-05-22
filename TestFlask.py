from flask import Flask, flash, redirect, render_template, request, session, abort
from random import *

app = Flask(__name__)

@app.route("/")
def hello(name):
    items = ["name1", "name2", "name3", "name4"]

    x = sample(items, 1)  # Pick a random item from the list
    name = x[0]
    return render_template(
        'test.html', name=x[0])


if __name__ == "__main__":
    app.run()
