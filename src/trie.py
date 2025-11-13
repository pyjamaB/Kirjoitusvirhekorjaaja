class Node:
    """Luokka, joka luo uuden trie-tietorakenteen solmun.
    Attribuutit:
        self.children: solmun lapsisolmut
        self.last_letter: palauttaa boolean-arvon, joka kertoo, onko
        solmu sanan viimeinen kirjain.
    """
    def __init__(self):
        """Luokan konstruktori
        """
        self.children = {}
        self.last_letter = False

class Trie:
    """Trie-tietorakennetta kuvaava luokka, johon tallennetaan sanaston sanat.
    Attribuutit:
        self.root: juurisolmu
    """
    def __init__(self):
        """Luokan konstruktori
        """
        self.root = Node()

    def add_word(self, word):
        """Luokan metodi, jolla lisätään sana tietorakenteeseen.
        Args:
            word: tietorakenteeseen tallennetava sana.
        """
        current_node = self.root
        for i in range(len(word)):
            if word[i] not in current_node.children:
                current_node.children[word[i]] = Node()
            current_node = current_node.children[word[i]]
        current_node.last_letter = True

    def search_word(self, word):
        """Luokan metodi, jolla voidaan etsiä sana trie-tietorakenteesta.
        Args:
            word: triestä etsittävä sana.
        Returns:
            bool: True, jos sana löytyy tietorakenteesta.
        """
        current_node = self.root
        for i in range(len(word)):
            if word[i] not in current_node.children:
                return False
            current_node = current_node.children[word[i]]
        return current_node.last_letter
