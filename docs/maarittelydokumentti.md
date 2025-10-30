# Määrittelydokumentti

Määrittelen tässä dokumentissa Helsingin yliopiston Aineopintojen harjoitustyö: Algoritmit ja tekoäly -kurssin harjoitustyöni. Teen harjoitustyöni osana tietojenkäsittelytieteen kandiohjelmaa (TKT).


## Harjoitustyön aihe ja toteutus

Harjoitustyöni aiheena on kirjoitusvirheiden korjaaja, joka korjaa käyttäjän tekstisyötteenä antamia sanoja. Työn ydin on siis algoritmi, joka vertaa käyttäjän syötteenä antamia sanoja ohjelman suomenkieliseen sanastoon ja mittaa etäisyyden oikein kirjoitettuun sanaan. Algoritmi tarjoaa myös ehdotuksia väärinkirjoitetun sanan korjaamiseksi etsimällä sanastosta lähimmän sanan.
Toteutan työni pythonilla, joka on ainoa ohjelmointikieli, jonka tällä hetkellä hallitsen riittävän hyvin. Hyödynnän työssäni kurssimateriaalissa mainittuja trie-tietorakennetta ja Damerau-Levenshteinin -etäisyysalgoritmia. Ohjelma saa syötteekseen käyttäjän ohjelmalle antamia yksittäisiä sanoja, joita verrataan trie-tietorakenteeseen tallennettuun sanastoon. Lähteiden perusteella trie-tietorakenteen aikavaativuus on O(n) ja Damerau-Levenshteinin -etäisyyden puolestaan O(m*n).

## Dokumentaation kieli

Kirjoitan harjoitustyön dokumentaation suomeksi.

## Lähteet

Alla on käyttämäni lähteet:

- [Wikipedian artikkeli triestä](https://en.wikipedia.org/wiki/Trie)
- [Wikipedian artikkeli Dameraun-Levenshteinin -etäisyydestä](https://en.wikipedia.org/wiki/Damerau–Levenshtein_distance)
- [Geeks for geeksin artikkeli Dameraun-Levenshteinin -etäisyydestä](https://www.geeksforgeeks.org/dsa/damerau-levenshtein-distance/)
