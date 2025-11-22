import unittest
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
        self.assertEqual(False, self.spellchecker.find_word(""))

    def test_find_all_words(self):
        list1 = ["testing"]
        list2 = ["testingagain"]
        list3 = ["testingoncemore"]
        self.assertEqual(list1, self.spellchecker.find_all_words("testingy", 1))
        self.assertEqual(list2, self.spellchecker.find_all_words("testingagai", 1))
        self.assertEqual(list3, self.spellchecker.find_all_words("testingoncemor", 1))
