import unittest
from spellchecker import SpellCheck

class TestSpellchecker(unittest.TestCase):
    def setUp(self):
        self.spellchecker = SpellCheck("src/wordfiles/joukahainen.xml")
        test_words = ["testing", "testingagain", "testingoncemore"]
        for word in test_words:
            self.spellchecker.trie.add_word(word)

    def test_find_word(self):
        self.assertEqual(self.spellchecker.find_word("testing"), True)
        self.assertEqual(self.spellchecker.find_word("testingagain"), True)
        self.assertEqual(self.spellchecker.find_word("testingoncemore"), True)
        self.assertEqual(self.spellchecker.find_word(""), False)

    def test_find_all_words(self):
        list1 = ["testing"]
        list2 = ["testingagain"]
        list3 = ["testingoncemore"]
        self.assertEqual(self.spellchecker.find_all_words("testingy", 1), list1)
        self.assertEqual(self.spellchecker.find_all_words("testingagai", 1), list2)
        self.assertEqual(self.spellchecker.find_all_words("tsetingoncemore", 1), list3)
        self.assertEqual(self.spellchecker.find_all_words("tasting", 1), list1)
        self.assertNotEqual(self.spellchecker.find_all_words("tastingy", 1), list1)
        self.assertNotEqual(self.spellchecker.find_all_words("tästing", 1), list1)
        self.assertNotEqual(self.spellchecker.find_all_words("testingoncmeore", 1), list3)
