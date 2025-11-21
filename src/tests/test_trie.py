import hypothesis.strategies as st
from hypothesis import given, settings
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
        self.assertEqual(False, self.trie.search_word(""))

    @given(arvo=st.text(alphabet="abcdefghijklmnopqrstyvwxyzåäö", min_size=1, max_size=35))    
    @settings(max_examples=500)
    def test_trie_hypothesis(self, arvo):
        h_trie = Trie()
        h_trie.add_word(arvo)
        assert h_trie.search_word(arvo)
