import unittest
from damerau_levenshtein import damerau_levenshtein

class TestDamerauLevenshtein(unittest.TestCase):
    def test_damerau_levenshtein(self):
        self.assertEqual(1, damerau_levenshtein("testi", "testit"))
        self.assertEqual(1, damerau_levenshtein("testi", "test"))
        self.assertEqual(0, damerau_levenshtein("testi", "testi"))
        self.assertEqual(5, damerau_levenshtein("", "testi"))
        self.assertEqual(0.9, damerau_levenshtein("tetsi", "testi"))
        self.assertEqual(1, damerau_levenshtein("testit", "testi"))
        self.assertEqual(1.4, damerau_levenshtein("tahti", "tuhti"))
        self.assertEqual(1.7, damerau_levenshtein("tähti", "tahti"))
