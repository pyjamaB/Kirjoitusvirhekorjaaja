import unittest
from trie import Trie

class TestTrie(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()
        self.trie.add_word("alfa")
        self.trie.add_word("beeta")
        self.trie.add_word("gamma")
        self.trie.add_word("yksi")
        self.trie.add_word("kaksi")
        self.trie.add_word("kolme")        

    def test_add_to_trie(self):
        self.assertEqual(True, self.trie.search_word("alfa"))
        self.assertEqual(True, self.trie.search_word("beeta"))
        self.assertEqual(True, self.trie.search_word("gamma"))
        self.assertEqual(True, self.trie.search_word("yksi"))
        self.assertEqual(True, self.trie.search_word("kaksi"))
        self.assertEqual(True, self.trie.search_word("kolme"))

    def test_search_from_trie(self):   
        self.assertEqual(True, self.trie.search_word("alfa"))
        self.assertEqual(True, self.trie.search_word("beeta"))
        self.assertEqual(True, self.trie.search_word("gamma"))
        self.assertEqual(True, self.trie.search_word("yksi"))
        self.assertEqual(True, self.trie.search_word("kaksi"))
        self.assertEqual(True, self.trie.search_word("kolme"))
        self.assertEqual(False, self.trie.search_word("neljä"))
