class DamerauLevenshtein:
    """Luokka, jonka avulla lasketaan Dameraun-Levenshteinin-etäisyys.
    """
    def __init__(self):
        """Luokan konstruktori, joka luo Damerau-Levenshtein-olion
        """
        letters = "qwertyuiopåasdfghjklöäzxcvbnm"
        self.distances = {}
        for letter in letters:
            self.distances[letter] = {}
        for letter1 in letters:
            for letter2 in letters:
                self.distances[letter1][letter2] = self.calculate_distance(letter1, letter2)

    def calculate_distance(self, key1, key2):
        """Funktio, joka laskee ensin kahden merkin välisen etäisyyden
        näppäimistöllä ja laskee etäisyyden perusteella painon transpoosille
        ja korvaukselle.
        Args:
            key1 ja key2: kirjaimet, joiden välinen etäisyys näppäimistöllä
            lasketaan.
        Returns:
            int: palauttaa kirjainten välille lasketun etäisyyden.
        """
        alphabet_keys = {"q": (0, 0), "w": (0, 1), "e": (0, 2), "r": (0, 3),
        "t": (0, 4), "y": (0, 5), "u": (0, 6), "i": (0, 7), "o": (0, 8),
        "p": (0, 9), "å": (0, 10), "a": (1, 0), "s": (1, 1), "d": (1, 2), "f": (1, 3),
        "g": (1, 4), "h": (1, 5), "j": (1, 6), "k": (1, 7), "l": (1, 8), "ö": (1, 9),
        "ä": (1, 10), "z": (2, 0), "x": (2, 1), "c": (2, 2), "v": (2, 3), "b": (2, 4),
        "n": (2, 5), "m": (2, 6)}

        value1 = alphabet_keys[key1]
        value2 = alphabet_keys[key2]
        key_distance =  abs(value1[0] - value2[0]) + abs(value1[1] - value2[1])
        return (0.1 * key_distance)

    def keyboard_distance(self, k1, k2, base_cost):
        """Funktio, joka laskee kirjainten välisten etäisyyksien
           perusteella painon transpoosille ja korvaukselle.
        Args:
            k1 ja k2: Kirjaimet joiden korvaukselle tai
            transpoosille paino lasketaan
            base_cost: pohja-arvo painon laskemista varten
        Returns:
            int: paino transpoosille tai korvaukselle
        """
        if k1 not in self.distances or k2 not in self.distances:
            return 2.0
        return self.distances[k1][k2] + base_cost

    def damerau_levenshtein(self, word1, word2):
        """Funktio, joka selvittää kahden sanan välisen etäisyyden.
        Args:
            word1 ja word2: kaksi sanaa, joiden välinen etäisyys selvitetään.
        Returns:
            int: palauttaa sanojen välisen etäisyyden.
        """
        distance = [[0 for j in range(len(word2) + 1)]
                   for i in range(len(word1) + 1)]

        for i in range(len(word1) + 1):
            distance[i][0] = i
        for j in range(len(word2) + 1):
            distance[0][j] = j

        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if word1[i - 1] == word2[j - 1]:
                    cost = 0
                else:
                    cost = self.keyboard_distance(word1[i - 1], word2[j - 1], 0.7)
                distance[i][j] = min(distance[i - 1][j] + 1,
                                     distance[i][j - 1] + 1,
                                     distance[i - 1][j - 1] + cost)
                if i > 1 and j > 1 and word1[i - 1] == word2[j - 2] and word1[i - 2] == word2[j - 1]:
                    distance[i][j] = min(distance[i][j],
                                         distance[i - 2][j - 2] +
                                         self.keyboard_distance(word1[i - 2], word1[i - 1], 0.5))
        return distance[len(word1)][len(word2)]
