import xml.etree.ElementTree as ET

def parse_words(xml_path):
    """Metodi joka poimii sanastotietokannan sanat xml-tiedostosta,
    ja palauttaa ne trie-tietorakenteeseen lisäämistä varten.
    Args:
        xml_path: xml-tiedoston sijainti hakemistossa.
    Returns:
        words: lista tietokannan sanoista.
    """
    tree = ET.parse(xml_path)
    root = tree.getroot()
    words = []

    for element in root.findall(".//form"):
        if element.text:
            words.append(element.text.strip())
    words.sort()
    return words
