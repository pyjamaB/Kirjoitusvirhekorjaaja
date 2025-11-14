from flask import Flask
from flask import abort, render_template, request
from spellchecker import SpellCheck

app = Flask(__name__)
spellchecker = SpellCheck("src/wordfiles/joukahainen.xml")

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
    if not word or len(word) > 35:
        abort(403)
    if spellchecker.find_word(word):
        result = "Sana on kirjoitettu oikein!"
        return render_template("correct.html", word=word , result=result)
    candidates = spellchecker.find_all_words(word, 1)
    candidates = sorted(candidates)
    if len(candidates) > 0:
        result = "Tarkoititko sanaa:"
    else:
        result = "Sanaa ei löytynyt."
    return render_template("correct.html", word=word, result=result, candidates=candidates)
