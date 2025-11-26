import unittest
import hypothesis.strategies as st
from hypothesis import given, settings
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

    def test_add_and_search_trie(self):
        self.assertEqual(True, self.trie.search_word("alfa"))
        self.assertEqual(True, self.trie.search_word("beeta"))
        self.assertEqual(True, self.trie.search_word("gamma"))
        self.assertEqual(True, self.trie.search_word("yksi"))
        self.assertEqual(True, self.trie.search_word("kaksi"))
        self.assertEqual(True, self.trie.search_word("kolme"))
        self.assertEqual(False, self.trie.search_word("neljä"))
        self.assertEqual(False, self.trie.search_word(""))

    def test_search_allwords_trie(self):
        def find_all_words(self):
            self.all_words_string = ""

            def visit_next_node(current_node, word):
                if current_node.last_letter:
                    self.all_words_string += word
                for letter in current_node.children:
                    visit_next_node(current_node.children[letter],
                                     word + letter)
            visit_next_node(self.trie.root, "")
            return self.all_words_string
        all_in_string = find_all_words(self)
        self.assertEqual("alfabeetagammayksikaksikolme", all_in_string)

    @given(arvo=st.text(alphabet="abcdefghijklmnopqrstyvwxyzåäö", min_size=1, max_size=35))
    @settings(max_examples=500)
    def test_trie_hypothesis(self, arvo):
        h_trie = Trie()
        h_trie.add_word(arvo)
        assert h_trie.search_word(arvo)
