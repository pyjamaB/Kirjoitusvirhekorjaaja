alphabet_keys = {"q": (0, 0), "w": (0, 1), "e": (0, 2), "r": (0, 3),
"t": (0, 4), "y": (0, 5), "u": (0, 6), "i": (0, 7), "o": (0, 8),
 "p": (0, 9), "å": (0, 10), "a": (1, 0), "s": (1, 1), "d": (1, 2), "f": (1, 3),
 "g": (1, 4), "h": (1, 5), "j": (1, 6), "k": (1, 7), "l": (1, 8), "ö": (1, 9),
 "ä": (1, 10), "z": (2, 0), "x": (2, 1), "c": (2, 2), "v": (2, 3), "b": (2, 4),
 "n": (2, 5), "m": (2, 6)}

def transposition_cost(key1, key2, alphabet_keys):
    """Funktio, joka laskee ensin kahden merkin välisen etäisyyden
    näppäimistöllä ja laskee etäisyyden perusteella painon transpoosille.
    Args:
        key1 ja key2: kirjaimet, joiden välinen etäisyys näppäimistöllä
        lasketaan.
        alphabet_keys: sanakirja, johon on talletettu näppäimistön
        kirjainten etäisyyskoordinaatit.
    Returns:
        int: palauttaa kirjainten välisen etäisyyden perusteella
        lasketun painon.
    """
    if key1 not in alphabet_keys or key2 not in alphabet_keys:
        return 2.0
    value1 = alphabet_keys[key1]
    value2 = alphabet_keys[key2]
    key_distance =  abs(value1[0] - value2[0]) + abs(value1[1] - value2[1])
    return 0.5 + (0.1 * key_distance)

def damerau_levenshtein(word1, word2):
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
            distance[i][j] = min(distance[i - 1][j] + 1,
                                 distance[i][j - 1] + 1,
                                 distance[i - 1][j - 1] + cost)
            if i > 1 and j > 1 and word1[i - 1] == word2[j - 2] and word1[i - 2] == word2[j - 1]:
                distance[i][j] = min(distance[i][j],
                                     distance[i - 2][j - 2] + 
                                     transposition_cost(word1[i - 2], word1[i - 1], alphabet_keys))
    return distance[len(word1)][len(word2)]
