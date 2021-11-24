from flask import Flask, request, redirect
from flask.helpers import url_for
from flask.wrappers import Response
import requests
import random
from random import randint

app = Flask(__name__)

# animal generator route here
@app.route("/animal/name", methods=["GET"])
def animal():
    names = ["Cat", "Dog", "Pig", "Cow", "Lion"]
    #or choice = animals[randint(0,2)]
    choice = random.choice(names)
    return Response(choice, mimetype="text/plain")



# animal noise generator route here
@app.route("/animal/noise", methods=["POST"])
def noise():
    animal= request.data.decode('utf-8')
    noises = {"Cat": "meow", "Dog": "woof", "Pig": "oink", "Cow": "moow", "Lion": "Roar!"}
    choice = noises[animal].title()
    return Response(choice, mimetype="text/plain")

## alternative method ->
    #if animal == "Cat"
    #   noise == "meow"
    #elif animal == "Dog"
    #   noise == "Woof"
    #return Response(noise, mimetype='ptext/plain')


    


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)