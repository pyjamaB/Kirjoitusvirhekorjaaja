import unittest
from damerau_levenshtein import DamerauLevenshtein

class TestDamerauLevenshtein(unittest.TestCase):
    def setUp(self):
        self.damerau = DamerauLevenshtein()
    def test_damerau_levenshtein_add_letter(self):
        self.assertAlmostEqual(self.damerau.damerau_levenshtein("testi", "testit"), 1.0)
    def test_damerau_levenshtein_remove_letter(self):
        self.assertAlmostEqual(self.damerau.damerau_levenshtein("testi", "test"), 1.0)
    def test_damerau_levenshtein_same_words(self):
        self.assertAlmostEqual(self.damerau.damerau_levenshtein("testi", "testi"), 0)
    def test_damerau_levenshtein_empty_string(self):
        self.assertAlmostEqual(self.damerau.damerau_levenshtein("", "testi"), 5.0)
    def test_damerau_levenshtein_transposition(self):
        self.assertAlmostEqual(self.damerau.damerau_levenshtein("tetsi", "testi"), 0.9)
    def test_damerau_levenshtein_add_letter_change_order(self):
        self.assertAlmostEqual(self.damerau.damerau_levenshtein("testit", "testi"), 1.0)
    def test_damerau_levenshtein_replace_letter(self):
        self.assertAlmostEqual(self.damerau.damerau_levenshtein("tahti", "tuhti"), 1.4)
    def test_damerau_levenshtein_replace_letter_unicode(self):
        self.assertAlmostEqual(self.damerau.damerau_levenshtein("tähti", "tahti"), 1.7)
    def test_damerau_levenshtein_add_letter_transposition(self):
        self.assertAlmostEqual(self.damerau.damerau_levenshtein("testi", "etstit"), 1.7)
    def test_damerau_levenshtein_add_letter_transpose_replace(self):
        self.assertAlmostEqual(self.damerau.damerau_levenshtein("abcdefg", "tabcedfh"), 2.4)
    def test_damerau_levenshtein_add_letter_remove(self):
        self.assertAlmostEqual(self.damerau.damerau_levenshtein("abcdefg", "tabcdef"), 2.0)
    def test_damerau_levenshtein_remove_letter_transposition(self):
        self.assertAlmostEqual(self.damerau.damerau_levenshtein("testi", "etst"), 1.7)
    def test_damerau_levenshtein_replace_add_letter(self):
        self.assertAlmostEqual(self.damerau.damerau_levenshtein("testi", "tastit"), 2.0)
    def test_damerau_levenshtein_replace_remove_letter(self):
        self.assertAlmostEqual(self.damerau.damerau_levenshtein("testi", "tast"), 2.0)
    def test_damerau_levenshtein_replace_transposition(self):
        self.assertAlmostEqual(self.damerau.damerau_levenshtein("testi", "tatsi"), 1.9)
    def test_damerau_levenshtein_add_letter_transpose_remove(self):
        self.assertAlmostEqual(self.damerau.damerau_levenshtein("abcdefg", "tabcedf"), 2.6)
    def test_calculate_distance(self):
        self.assertEqual(self.damerau.calculate_distance("w", "e"), 1)
    def test_calculate_distance(self):
        self.assertEqual(self.damerau.calculate_distance("q", "d"), 3)
    def test_keyboard_distance_transpose(self):
        self.assertAlmostEqual(self.damerau.keyboard_distance("q", "m", 0.5), 1.3)
    def test_keyboard_distance_replacement(self):
        self.assertAlmostEqual(self.damerau.keyboard_distance("w", "r", 0.7), 0.9)
