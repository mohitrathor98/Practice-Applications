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
    
    inp = request.form.get('choice-field')
    value = valid_input(inp)
    if value == -1:
        return html_codes.error_body
    if value == actualNum:
        return html_codes.success_body
    elif value > actualNum:
        return html_codes.high_value_body
    else:
        return html_codes.low_value_body
    
@app.route('/game-restart', methods=['POST'])
def restart_game():
    return landing()

def valid_input(inp):
    if not inp.isdigit():
        return -1
    value = int(inp)
    if value > 9 or value < 0:
        return -1
    return value

if __name__ == "__main__":
    app.run(debug=True)