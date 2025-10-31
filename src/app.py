from flask import Flask
from flask import abort, redirect, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    """Palauttaa sivun index.html
    Returns:
        index.html sivu
    """

    return render_template("index.html")
    
@app.route("/check_typos", methods=["POST"])
def check_typos():
    """Saa käyttäjältä syötteenä tarkistettavan sanan
    ja tarkistaa oikeinkirjoituksen
    Returns:
        palauttaa sivun correct.html, joka sisältää
    arvion sanan oikeinkirjoituksesta
    """

    word = request.form["word"]
    if not word or len(word) > 25:
        abort(403)
    return render_template("correct.html", word=word)
