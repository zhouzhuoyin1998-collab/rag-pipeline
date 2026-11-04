"""
RAG Pipeline

Assembled from your step-by-step solutions.
"""

import numpy as np

# Step 1 - load_text_file
def load_text_file(path):
    # TODO: read a UTF-8 text file at `path` and return its contents as one string.
    with open(path, "r", encoding="utf-8") as file:
        return file.read()

# Step 2 - load_text_directory
def load_text_directory(directory):
    # TODO: read every .txt file in `directory` and return their contents as a list of strings
    results = []

    for filename in sorted(os.listdir(directory)):
        if filename.endswith(".txt"):
            path = os.path.join(directory, filename)
            results.append(load_text_file(path))

    return results

# Step 3 - extract_text_from_html
from html.parser import HTMLParser

class TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text = []
        self.skip = False

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style"):
            self.skip = True

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self.skip = False

    def handle_data(self, data):
        if not self.skip:
            self.text.append(data)


def extract_text_from_html(html):
    parser = TextExtractor()
    parser.feed(html)
    return "".join(parser.text).strip()

# Step 4 - normalize_text
import unicodedata
def normalize_text(text):
    # TODO: NFKC-normalize the text and collapse runs of whitespace into single spaces.
    
    text = unicodedata.normalize("NFKC", text)

    # Step 2: Collapse whitespace and strip edges
    text = " ".join(text.split())

    return text

