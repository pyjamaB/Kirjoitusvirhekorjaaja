# Testausdokumentti

## Yksikkötestaus
Projektin yksikkötestauksessa on käytetty unittest-kehystä, jonka avulla on testattu src-hakemistossa olevia luokkia ja funktioita. Käyttöliittymän toiminta on rajattu automaattistentestien ulkopuolelle. Src-hakemistossa automaattiset testit testaavat trie-tietorakenteeseen, Damerau-Levenshteinin -etäisyysalgoritmiin sekä sanan oikeinkirjoituksen tarkastamiseen liittyviä toimintoja. Testit testaavat sovelluksen toimintaa sekä oikeanmuotoisilla että virheellisillä syötteillä.
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
