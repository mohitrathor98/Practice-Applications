from flask import Flask, request
import html_codes
import random

app = Flask(__name__)

actualNum = -1

@app.route('/')
def landing():
    global actualNum

    actualNum = random.randint(0, 9)
    return html_codes.landing_body

@app.route('/submit-form', methods=['POST'])
def submit_form():
    global actualNum
    value = int(request.form.get('choice-field'))
    if value == actualNum:
        #success page
        return "Yep"
    elif value > actualNum:
        # Lower page
        return "Go lower"
    else:
        # Higher page
        return "Go higher"

if __name__ == "__main__":
    app.run(debug=True)