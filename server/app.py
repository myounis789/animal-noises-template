from flask import Flask, render_template
from flask.globals import request, Response
from jinja2.utils import pass_context

app = Flask(__name__)

# home route here

@app.route("/")
def home():
    return render_template("index.html")

# must query the animal API for an animal and a noise – the noise should be based on the animal

# MAKES A GET REQUEST FOR ANIMAL
@app.route("/http:xxxx/animal", methods=["GET" , "POST"])
def animal_get():
    if request.method == "GET":
    #needs to get animal from api server
        return Response("Your animal is", mimetype="text/plain")
    #needs to get animal, and assign animal to correct noise.
    #return animal an noise.
    if request.method == ["POST"]:

# MAKES A POST REQUEST FOR ANIMAL NOISE
    #needs to get animal, and assign animal to correct noise.
    #return animal an noise.


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)