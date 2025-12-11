import unittest
from damerau_levenshtein import DamerauLevenshtein

class TestDamerauLevenshtein(unittest.TestCase):
    def setUp(self):
        self.damerau = DamerauLevenshtein()
    def test_damerau_levenshtein_add_letter(self):
        self.assertEqual(1, self.damerau.damerau_levenshtein("testi", "testit"))
    def test_damerau_levenshtein_remove_letter(self):
        self.assertEqual(1, self.damerau.damerau_levenshtein("testi", "test"))
    def test_damerau_levenshtein_same_words(self):
        self.assertEqual(0, self.damerau.damerau_levenshtein("testi", "testi"))
    def test_damerau_levenshtein_empty_string(self):
        self.assertEqual(5, self.damerau.damerau_levenshtein("", "testi"))
    def test_damerau_levenshtein_transposition(self):
        self.assertEqual(0.9, self.damerau.damerau_levenshtein("tetsi", "testi"))
    def test_damerau_levenshtein_add_letter_change_order(self):
        self.assertEqual(1, self.damerau.damerau_levenshtein("testit", "testi"))
    def test_damerau_levenshtein_replace_letter(self):
        self.assertEqual(1.4, self.damerau.damerau_levenshtein("tahti", "tuhti"))
    def test_damerau_levenshtein_replace_letter_unicode(self):
        self.assertEqual(1.7, self.damerau.damerau_levenshtein("tähti", "tahti"))
    def test_damerau_levenshtein_add_letter_transposition(self):
        self.assertEqual(1.7, self.damerau.damerau_levenshtein("testi", "etstit"))
    def test_damerau_levenshtein_add_letter_transpose_replace(self):
        self.assertEqual(2.4, self.damerau.damerau_levenshtein("abcdefg", "tabcedfh"))
    def test_damerau_levenshtein_add_letter_remove(self):
        self.assertEqual(2, self.damerau.damerau_levenshtein("abcdefg", "tabcdef"))
    def test_damerau_levenshtein_remove_letter_transposition(self):
        self.assertEqual(1.7, self.damerau.damerau_levenshtein("testi", "etst"))
    def test_damerau_levenshtein_replace_add_letter(self):
        self.assertEqual(2, self.damerau.damerau_levenshtein("testi", "tastit"))
    def test_damerau_levenshtein_replace_remove_letter(self):
        self.assertEqual(2, self.damerau.damerau_levenshtein("testi", "tast"))
    def test_damerau_levenshtein_replace_transposition(self):
        self.assertEqual(1.9, self.damerau.damerau_levenshtein("testi", "tatsi"))
    def test_damerau_levenshtein_add_letter_transpose_remove(self):
        self.assertEqual(2.6, self.damerau.damerau_levenshtein("abcdefg", "tabcedf"))
