import subprocess
import sys

# Function to install packages
def install_packages():
    try:
        import requests
        import bs4
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "requests", "beautifulsoup4"])
        print("Installed required packages.")

install_packages()

import requests
from bs4 import BeautifulSoup
import time
import random

BASE_URL = "https://www.wordexample.com/list/"
WORD_TYPES = {
    "adjectives": "adjectives",
    "adverbs": "adverbs",
    "nouns": "nouns"
}

HEADERS = {'User-Agent': 'Mozilla/5.0'}

def scrape_words(word_type: str, pages: int = 3):
    words = []
    for page in range(1, pages + 1):
        url = f"{BASE_URL}{word_type}?page={page}"
        print(f"Scraping {word_type} - Page {page}")
        response = requests.get(url, headers=HEADERS)
        if response.status_code != 200:
            print(f"Failed to load page {page} for {word_type}")
            continue
        soup = BeautifulSoup(response.text, 'html.parser')
        word_elements = soup.select("div.word-list > ul > li")
        words_on_page = [w.text.strip() for w in word_elements if w.text.strip()]
        words.extend(words_on_page)
        time.sleep(1)  # Be nice to the server
    return words

def get_word_lists():
    adjectives = scrape_words("adjectives", pages=3)
    adverbs = scrape_words("adverbs", pages=3)
    nouns = scrape_words("nouns", pages=3)
    return adjectives, adverbs, nouns

# Example usage
if __name__ == "__main__":
    adjectives, adverbs, nouns = get_word_lists()
    print(f"Got {len(adjectives)} adjectives, {len(adverbs)} adverbs, and {len(nouns)} nouns.")
    # Example preview
    print("Adjectives sample:", adjectives[:10])
    print("Adverbs sample:", adverbs[:10])
    print("Nouns sample:", nouns[:10])
    print(f"I invite you to consider a new name: {random.choice(adverbs)} {random.choice(adjectives)} {random.choice(adjectives)}")