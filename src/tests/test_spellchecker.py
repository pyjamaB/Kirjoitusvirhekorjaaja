import unittest
from trie import Trie
import damerau_levenshtein
from spellchecker import SpellCheck

class TestSpellchecker(unittest.TestCase):
    def setUp(self):
        self.spellchecker = SpellCheck("src/wordfiles/joukahainen.xml")
        test_words = ["testing", "testingagain", "testingoncemore"]
        for word in test_words:
            self.spellchecker.trie.add_word(word)
    
    def test_find_word(self):
        self.assertEqual(True, self.spellchecker.find_word("testing"))
        self.assertEqual(True, self.spellchecker.find_word("testingagain"))
        self.assertEqual(True, self.spellchecker.find_word("testingoncemore"))

    def test_find_all_words(self):
        set1 = {"testing"}
        set2 = {"testingagain"}
        set3 = {"testingoncemore"}
        self.assertEqual(set1, self.spellchecker.find_all_words("testingy", 1))
        self.assertEqual(set2, self.spellchecker.find_all_words("testingagai", 1))
        self.assertEqual(set3, self.spellchecker.find_all_words("testingoncemor", 1))
