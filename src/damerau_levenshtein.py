class damerau_levenshtein_distance:
    """Luokka, jolla selvitetään Damerau_Levenshteinin etäisyys.
    """
    def __init__(self):
        """Luokan konstruktori.
        """
        pass

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
                    cost = 1
                distance[i][j] = min(distance[i-1][j] + 1,
                                     distance[i][j-1] + 1,
                                     distance[i-1][j-1] + cost)
                if i > 1 and j > 1 and word1[i - 1] == word2[j - 2] and word1[i - 2] == word2[j - 1]:
                    distance[i][j] = min(distance[i][j],
                                         distance[i - 2][j - 2] + cost)
        return distance[len(word1)][ len(word2)]
