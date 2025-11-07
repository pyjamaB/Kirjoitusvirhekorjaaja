from flask import Flask
from flask import abort, redirect, render_template, request
from trie import Trie, Node
from damerau_levenshtein import damerau_levenshtein_distance
import vocabulary

app = Flask(__name__)
trie = Trie()
words = vocabulary.parse_words("src/wordfiles/joukahainen.xml")
for word in words:
    trie.add_word(word)

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
    if trie.search_word(word):
        result = "Sana on kirjoitettu oikein!"
        return render_template("correct.html", word=word , result=result)
    else:
        candidates= []
        for word2 in words:
            suggested = damerau_levenshtein_distance()
            if suggested.damerau_levenshtein(word, word2) <= 1:
                candidates.append(word2)
        if len(candidates) > 0:
            result = "Tarkoititko sanaa:"
        else:
            result = "Sanaa ei löytynyt."
        return render_template("correct.html", word=word, result=result, candidates=candidates)
