import xml.etree.ElementTree as ET

def parse_words(xml_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()
    words = []

    for element in root.findall(".//form"):
        if element.text:
            words.append(element.text.strip())
    words.sort()
    return words
