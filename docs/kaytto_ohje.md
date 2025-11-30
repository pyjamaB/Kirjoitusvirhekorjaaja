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
Tämän jälkeen voit avata selaimen ja siirtyä komentorivin antamaan osoitteeseen. Saat suljettua paikallisesti ajettavan sovelluksen komennolla ctrl + c.

Ohjelman testit voit ajaa komennolla:
```
pytest src
```
Virtuaaliympäristöstä pääset lopuksi pois kirjoittamalla komennon exit komentoriville.
