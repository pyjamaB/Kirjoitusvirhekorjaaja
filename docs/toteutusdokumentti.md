# Toteutusdokumentti

## Ohjelman rakenne

Sovellus on kirjoitusvirheiden korjaaja, joka saa syötteekseen käyttäjältä yksittäisiä sanoja, joista sovellus tarkistaa niiden oikeinkirjoituksen. Ohjelma etsii syötteenä saatua sanaa ensin trie-tietorakenteesta. Jos sana löytyy, ohjelma ilmoittaa, että sana on kirjoitettu oikein. Jos sanaa ei löydy trie-tietorakenteesta, ohjelma palauttaa listan lähellä olevia sanoja vertaamalla syötteenä saatua sanaa trie-tietorakenteen sanoihin ja laskemalla sanojen välisen etäisyyden Dameraun-Levenshteinin -etäisyysalgoritmin avulla.

Tiedosto app.py sisältää ohjelman käyttöliittymän, joka on toteutettu verkkopohjaisena flaskin avulla. App.py palauttaa ensin index.html-sivun, jolle käyttäjä syöttää tarkistettavan sanan. Kun sana on syötetty, app.py ohjaa käyttäjän correct.html-sivulle, joka kertoo, onko sana kirjoitettu oikein ja tarjoaa tarvittaessa ehdotukset sanan korjaamiseksi. Tiedostot trie.py ja damerau_levenshtein.py sisältävät trie-tietorakenteen luovan koodin ja Damerau-Levenshteinin-etäisyysalgoritmin, joka laskee kahden verrattavan sanan välisen etäisyyden. Tiedosto spellchecker.py sisältää luokan SpellCheck, joka vastaa sanaston lataamisesta trie-tietorakenteeseen ja sanan oikeinkirjoituksen tarkistamisesta tiedostojen trie.py ja damerau_levenshtein.py avulla.


## Aika- ja tilavaativuudet

Verkosta hankitun tiedon perusteella trie-tietorakenteen aikavaativuus on O(n). Dameraun-Levenshteinin -etäisyyden aikavaativuus on puolestaan O(m*n).

# #Sovelluksen puutteet ja parannusehdotukset

Sovelluksella voi nähdä olevan useita puutteita, joita voisi jatkossa parantaa. Ensinnäkin sovellus korjaa vain yksittäisiä sanoja eikä pidempiä tekstinpätkiä. Ohjelmaa on mahdollista muokata kohtalaisen pienellä vaivalla niin, että se kykenisi korjaamaan useampia sanoja kerralla. Toisaalta ohjelma toimii ainoastaan suomenkielisellä sanastolla. Jatkossa ohjelmaa voisi tarvittaessa muokata niin, että käyttäjä voisi valita haluamansa kielen, jolloin ohjelma voisi korjata myös muilla kielillä kirjoitettuja sanoja. Ohjelma ei myöskään ota huomioon sanojen taivutuksia, vaan se vertaa korjattavia sanoja ainoastaan sanastosta löytyviin perusmuotoisiin sanoihin. Jatkossa sovellusta voisi yrittää kehittää niin, että se osaisi korjata myös taivutettuja sanoja. Neljäs ohjelman puute on se, että se tarjoaa korjausehdotukset sanalistana sen sijaan, että se korjaisi sanat automaattisesti. Jotta sovellusta olisi sujuvampi käyttää, se voisi tarjota käyttäjälle suoraan vaihtoehdon korjauksesta tekstin joukkoon, ja käyttäjä voisi tarvittaessa muokata vielä korjausta, jos se ei ole käyttäjän tarkoittama sana.

## Laajojen kielimallien käyttö

Projektin toteuttamisessa ei ole käytetty laajoja kielimalleja.

## Lähteet

- [Wikipedian artikkeli triestä](https://en.wikipedia.org/wiki/Trie)
- [Wikipedian artikkeli Dameraun-Levenshteinin -etäisyydestä](https://en.wikipedia.org/wiki/Damerau–Levenshtein_distance)
- [Geeks for geeksin artikkeli Dameraun-Levenshteinin -etäisyydestä](https://www.geeksforgeeks.org/dsa/damerau-levenshtein-distance/)
- [Geeks for geeksin artikkeli triestä](https://www.geeksforgeeks.org/dsa/trie-insert-and-search/)
