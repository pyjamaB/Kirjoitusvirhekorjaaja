# Käyttöohjeet

Kloonaa ensin projektin repositorio koneellesi ja siirry projektin hakemistoon. Varmista, että koneellesi on asennettu poetry, jonka jälkeen voit alustaa ohjelman riippuvuudet komennolla:
```
poetry install
```
Siirry virtuaaliympäristöön komennolla:
```
poetry shell
```
Tämän jälkeen voit käynnistää ohjelman komennolla:
```
python3 src/index.py
```
Tämän jälkeen voit avata selaimen ja siirtyä komentorivin antamaan osoitteeseen. Ohjelma tarkistaa oikeinkirjoituksen yksittäisistä sanoista. Syötettävän merkkijonon suurin sallittu pituus on 35 merkkiä. Saat suljettua paikallisesti ajettavan sovelluksen komennolla ctrl + c.

Ohjelman testit voit ajaa virtuaaliympäristössä komennolla:
```
pytest src
```
Testikattavuuden saa kerättyä virtuaaliympäristössä komennolla:
```
coverage run --branch -m pytest src
```
Edellisen komennon jälkeen raportin testikattavuudesta saa tulostettua komennolla:
```
coverage report -m
```
Virtuaaliympäristöstä pääset lopuksi pois kirjoittamalla komennon exit komentoriville.
