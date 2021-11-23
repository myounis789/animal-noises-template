from flask import Flask
import random

app = Flask(__name__)

# animal generator route here
@app.route
def animal():
    names = ["Cat", "Dog", "Pig", "Cow", "Lion"]
    choice = random.choice(names)
    return choice


animal = animal()
print(animal)





# animal noise generator route here
@app.route
def noise():
    noises = {"Cat": "meow", "Dog": "woof", "Pig": "oink", "Cow": "moow", "Lion": "Roar!"}
    choice = noises[animal].title()
    return choice

noise = noise()
print(noise)
    


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)