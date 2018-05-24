from flask import Flask, flash, redirect, render_template, request, session, abort
from random import *

app = Flask(__name__)

@app.route("/")
def hello(name):
    items = ["Mike Ferguson", "Viktor Titenko", "Susan Sexton", "Dustin Bench", "Marolynne Webb", "Scott Vossler",
             "Jason Theis", "Aaron Botello", "Berry Kroeger", "Doug Smith", "Brett Mortensen", "Alta Wright",
             "Cody Schiemann", "Dennis Burke", "Bryan McAdams", "Joe DiCola", "Patrick Dunlap", "Brandon Hudson",
             "Chris Dodd", "Robert Christensen", "Marcelo Stefani", "Jim Murray", "Rodney Brown", "Chris Keener",
             "Jack Yi"]

    x = sample(items, 1)  # Pick a random item from the list
    name = x[0]
    return render_template(
        'test.html', name=x[0])


if __name__ == "__main__":
    app.run()