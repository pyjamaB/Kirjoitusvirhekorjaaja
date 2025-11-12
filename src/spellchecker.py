from trie import Trie
import damerau_levenshtein
import xml.etree.ElementTree as ET

class SpellCheck:
    def __init__(self, xml_path):
        """Luokan konstruktori, joka poimii sanastotietokannan sanat xml-tiedostosta,
        ja palauttaa ne trie-tietorakenteeseen lisäämistä varten.
        Args:
            xml_path: xml-tiedoston sijainti hakemistossa.
        """
        self.trie = Trie()
        tree = ET.parse(xml_path)
        root = tree.getroot()
        words = []

        for element in root.findall(".//form"):
            if element.text:
                words.append(element.text.strip())
        words.sort()
        for word in words:
            self.trie.add_word(word)
    
    def find_word(self, input_word):
        return self.trie.search_word(input_word)

    def find_all_words(self, input_word, max_distance):
        """Luokan metodi, joka vertaa käyttäjän antamaa sanaa
           trie-tietorakenteesta löytyviin sanoihin ja laskee
           Dameraul-Levenshteinin algoritmin avulla etäisyyden sanojen välille.
        Args:
            input_word: käyttäjän antama sana.
            max_distance: pisin sallittu etäisyys verrattavien sanojen välillä.
        Returns:
            self.all_words: sanojen joukko, joka on halutun etäisyyden päässä
            käyttäjän antamasta sanasta.
        """
        self.all_words = set()

        def visit_next_node(current_node, word):
            if current_node.last_letter:
                distance = damerau_levenshtein.damerau_levenshtein(input_word, word)
                if distance <= max_distance:
                    self.all_words.add(word)
            for letter in current_node.children:
                visit_next_node(current_node.children[letter],
                                     word + letter)
        visit_next_node(self.trie.root, "")
        return self.all_words
