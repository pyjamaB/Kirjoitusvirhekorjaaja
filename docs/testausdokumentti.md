# Testausdokumentti

## Yksikkötestaus
Projektin yksikkötestauksessa on käytetty unittest-kehystä, jonka avulla on testattu src-hakemistossa olevia luokkia ja funktioita. Käyttöliittymän toiminta on rajattu automaattistentestien ulkopuolelle. Src-hakemistossa automaattiset testit testaavat trie-tietorakenteeseen, Damerau-Levenshteinin -etäisyysalgoritmiin sekä sanan oikeinkirjoituksen tarkastamiseen liittyviä toimintoja. Testit testaavat sovelluksen toimintaa sekä oikeanmuotoisilla että virheellisillä syötteillä.
### Testikattavuus
Alla on sovelluksen testikattavuusraportti:
```
Name                         Stmts   Miss Branch BrPart  Cover   Missing
------------------------------------------------------------------------
src/damerau_levenshtein.py      15      0     12      0   100%
src/spellchecker.py             28     28     12      0     0%   1-61
src/trie.py                     21      0      8      0   100%
------------------------------------------------------------------------
TOTAL                           64     28     32      0    58%
```
## Käyttöliittymän testaus
