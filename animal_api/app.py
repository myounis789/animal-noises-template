from flask import Flask, request, redirect
from flask.helpers import url_for
import requests
import random

app = Flask(__name__)

# animal generator route here
@app.route("/animal", methods=["GET"])
def animal():
    names = ["Cat", "Dog", "Pig", "Cow", "Lion"]
    choice = random.choice(names)
    return choice



# animal noise generator route here
@app.route("/animal", methods=["POST"])
def noise():
    animal= request.data.decode('utf-8')
    noises = {"Cat": "meow", "Dog": "woof", "Pig": "oink", "Cow": "moow", "Lion": "Roar!"}
    choice = noises[animal].title()
    return choice


    


if __name__ == "__main__":
    app.run(port=5000, debug=True)