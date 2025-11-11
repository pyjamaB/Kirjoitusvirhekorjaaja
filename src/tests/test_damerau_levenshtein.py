import unittest
from damerau_levenshtein import DamerauLevenshteinDistance

class TestDamerauLevenshtein(unittest.TestCase):
    def setUp(self):
        self.damerau_levenshtein = DamerauLevenshteinDistance()
    
    def test_damerau_levenshtein(self):
        self.assertEqual(1, self.damerau_levenshtein.damerau_levenshtein("testi", "testit"))
