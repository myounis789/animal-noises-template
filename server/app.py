from flask import Flask, render_template
from flask.globals import request, Response
from jinja2.utils import pass_context

app = Flask(__name__)

# home route here

@app.route("/")
def home():
    animal = request.get_data()
    noise = request.get_data()
    record= {1 : animal, 2 : noise}
    return render_template("index.html", data = record )

# must query the animal API for an animal and a noise – the noise should be based on the animal

# MAKES A GET REQUEST FOR ANIMAL
@app.route("/http:xxxx/animal", methods=["GET"])
def animal_get():
    #needs to get animal from api server
    animal= Response("Your animal is", mimetype="text/plain")
    #needs to get animal, and assign animal to correct noise.
    #return animal an noise.

# MAKES A POST REQUEST FOR ANIMAL NOISE
@app.route("/http:bbbb/animal", methods=["POST"])

    #needs to get animal, and assign animal to correct noise.
    #return animal an noise.


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)