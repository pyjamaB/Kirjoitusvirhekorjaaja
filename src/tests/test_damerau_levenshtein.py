import unittest
from damerau_levenshtein import damerau_levenshtein

class TestDamerauLevenshtein(unittest.TestCase):
    def test_damerau_levenshtein(self):
        self.assertEqual(1, damerau_levenshtein("testi", "testit"))
        self.assertEqual(0, damerau_levenshtein("testi", "testi"))
