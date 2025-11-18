# Testausdokumentti

## Yksikkötestaus
Projektin yksikkötestauksessa on käytetty unittest-kehystä, jonka avulla on testattu src-hakemistossa olevia luokkia ja funktioita. Käyttöliittymän toiminta on rajattu automaattisten testien ulkopuolelle. Src-hakemistossa automaattiset testit testaavat trie-tietorakenteeseen, Damerau-Levenshteinin -etäisyysalgoritmiin sekä sanan oikeinkirjoituksen tarkastamiseen liittyviä toimintoja. Testit testaavat sovelluksen toimintaa sekä oikeanmuotoisilla että virheellisillä syötteillä. Trie-tietorakenteesta on testattu, että ohjelma tallentaa sanat oikein ja myös palauttaa sanat oikein, kun käyttäjä etsii sanaa tietorakenteesta. Damerau-Levenshteinin algoritmista on testattu, että ohjelma laskee oikein haettavien sanojen välisen etäisyyden erilaisilla syötteillä. Kirjoitusvirheiden korjaamisen toiminnot yhdistävästä tiedostosta spellchecker.py on testattu, että se hakee oikein trie-tietorakenteesta löytyvät sanat ja palauttaa oikein listan haettavaa sanaa lähellä olevista sanoista, jos haettavaa sanaa ei löydy trie-tietorakenteesta.
### Testikattavuus
Alla on sovelluksen testikattavuusraportti:
```
Name                         Stmts   Miss Branch BrPart  Cover   Missing
------------------------------------------------------------------------
src/damerau_levenshtein.py      15      0     12      0   100%
src/spellchecker.py             28      0     12      1    98%   23->22
src/trie.py                     23      0      8      0   100%
------------------------------------------------------------------------
TOTAL                           66      0     32      1    99%
```
## Käyttöliittymän testaus
