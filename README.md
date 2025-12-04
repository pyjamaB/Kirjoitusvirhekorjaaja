# Kirjoitusvirhekorjaaja
Tämä on Helsingin yliopiston tietojenkäsittelytieteen kandiohjelman Aineopintojen harjoitustyö: Algoritmit ja tekoäly -kurssilla toteutettava harjoitustyö.

## Dokumentaatio
[Määrittelydokumentti](docs/maarittelydokumentti.md)

[Testausdokumentti](docs/testausdokumentti.md)

[Toteutusdokumentti](docs/toteutusdokumentti.md)

[Käyttöohje](docs/kaytto_ohje.md)
## Viikkoraportit
[Viikkoraportti 1](docs/viikkoraportti1.md)

[Viikkoraportti 2](docs/viikkoraportti2.md)

[Viikkoraportti 3](docs/viikkoraportti3.md)

[Viikkoraportti 4](docs/viikkoraportti4.md)

[Viikkoraportti 5](docs/viikkoraportti5.md)

[Viikkoraportti 6](docs/viikkoraportti6.md)
## Käyttöohjeet
Kloonaa ensin projektin repositorio koneellesi ja siirry projektin hakemistoon, jonka jälkeen voit alustaa ohjelman riippuvuudet komennolla:
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
