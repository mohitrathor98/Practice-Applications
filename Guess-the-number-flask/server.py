from flask import Flask, request
import html_codes
import random

app = Flask(__name__)

actualNum = -1
attempts = 0

@app.route('/')
def landing():
    global actualNum
    global attempts

    attempts = 0
    actualNum = random.randint(0, 9)
    return html_codes.landing_body

@app.route('/submit-form', methods=['POST'])
def submit_form():
    global actualNum
    global attempts

    attempts += 1
    
    inp = request.form.get('choice-field')
    value = valid_input(inp)
    if value == -1:
        # error page
        return "Please enter values between 0 to 9"
    if value == actualNum:
        return "Found it in {} attempts!!".format(attempts)
    elif value > actualNum:
        return html_codes.high_value_body
    else:
        return html_codes.low_value_body

def valid_input(inp):
    if not inp.isdigit():
        return -1
    value = int(inp)
    if value > 9 or value < 0:
        return -1
    return value

if __name__ == "__main__":
    app.run(debug=True)