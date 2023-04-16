from flask import Flask, render_template
from api import guessAge, guessGender

app = Flask(__name__)

@app.route("/guess/<name>")
def guessGenderAndAge(name):
    return render_template("index.html", name=str.capitalize(name), gender=guessGender(name), age=guessAge(name))


@app.route("/guess")
def guessPage():
    text = "<h1>You need to enter your name after guess.<h1></hr>"
    text += "<p>Ex: <em>guess/mohit</em></p>" 
    return text

@app.route("/")
def rootPage():
    text = "<h1>Nothing to see here.</h1> <hr>" 
    text += "<h2>Please provide guess in URL to see more.</h2>"
    return text


@app.errorhandler(404)
def pageNotFound(e):
    return "Something went wrong! Need to provide /guess/Name in URL."


if __name__ == "__main__":
    app.run(debug=True)