from flask import Flask
app = Flask(__name__)
import random

random_number = random.randint(0, 9)

@app.route('/')
def home():
    return "<h1 style='text-align: center'>Guess the number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/fDUOY00YvlhvtvJIVm/giphy.gif' width='200'/>"

@app.route('/random/<int:number>')
def user_guess(number):
    if number < random_number:
        return "<h1 style='color: red'>The number is too low, try again!</h1>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>"
    elif number > random_number:
        return "<h1 style='color: purple'>The number is too high, try again!</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>"
    else:
        return "<h1 style='color: green'>You found me!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"




if __name__ == "__main__":
    app.run(debug=True)

