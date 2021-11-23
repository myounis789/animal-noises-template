from flask import Flask

app = Flask(__name__)

# home route here

@app.route
def home():

    return 

# must query the animal API for an animal and a noise – the noise should be based on the animal

# MAKES A GET REQUEST FOR ANIMAL
@app.route
def animal_get():
    pass



# MAKES A POST REQUEST FOR ANIMAL NOISE
@app.route('/noise')
def noise_post():



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)