from flask import Flask, render_template
from flask.globals import request
import requests
from jinja2.utils import pass_context

app = Flask(__name__)

# home route here
@app.route("/", methods=['GET'])
def home_animal():
    # http:// <container name> so that docker network will direct to 
    animal = requests.get('http://api:5000/animal/name')
    noise = requests.post('http://api:5000/animal/noise', data=animal.text)
    #record = {1 : animal, 2 : noise}   Alternative way with json?
    return render_template("index.html", animal=animal.text , noise=noise.text )

# must query the animal API for an animal and a noise – the noise should be based on the animal

# MAKES A GET REQUEST FOR ANIMAL
#@app.route("/http:xxxx/animal", methods=["GET"])
#def animal_get():
    #needs to get animal from api server
    animal= Response("Your animal is", mimetype="text/plain")
    #needs to get animal, and assign animal to correct noise.
    #return animal an noise.

# MAKES A POST REQUEST FOR ANIMAL NOISE
#@app.route("/http:bbbb/animal", methods=["POST"])

    #needs to get animal, and assign animal to correct noise.
    #return animal an noise.


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)