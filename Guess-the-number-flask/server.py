from flask import Flask, request
import html_codes

app = Flask(__name__)

@app.route('/')
def landing():
    return html_codes.landing_body

@app.route('/submit-form', methods=['POST'])
def submit_form():
    return request.form.get('choice-field')

if __name__ == "__main__":
    app.run(debug=True)