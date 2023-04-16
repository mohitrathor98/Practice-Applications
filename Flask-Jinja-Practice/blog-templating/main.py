from flask import Flask, render_template
from post import Post

app = Flask(__name__)
postObj = Post()

@app.route('/')
def home():
    return render_template("index.html", allPosts=postObj.getData())

@app.route("/post/<id>")
def getDataById(id):
    return render_template("post.html", post=postObj.getPostById(id))

if __name__ == "__main__":
    app.run(debug=True)
