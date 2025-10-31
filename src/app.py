from flask import Flask
from flask import abort, flash, make_response, redirect, render_template, request

app = Flask(__name__)

@app.route("/")
def index():

    return render_template("index.html")
    
@app.route("/check_typos", methods=["POST"])
def check_typos():
    word = request.form["word"]
    if not word or len(word) > 25:
        abort(403)
    return render_template("correct.html", word=word)
