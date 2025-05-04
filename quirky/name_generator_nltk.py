import subprocess
import sys
import random

# Install nltk if needed
try:
    import nltk
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "nltk"])
    import nltk

# Download necessary NLTK resources
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('averaged_perceptron_tagger')

from nltk.corpus import wordnet as wn

# Helper function to get words by part of speech
def get_words_by_pos(pos_tag):
    words = set()
    for synset in wn.all_synsets(pos_tag):
        for lemma in synset.lemmas():
            word = lemma.name().replace('_', ' ').lower()
            if word.isalpha():  # ignore punctuation/numbers
                words.add(word)
    return sorted(words)

# Get large lists
nouns = get_words_by_pos('n')
adjectives = get_words_by_pos('a')
adverbs = get_words_by_pos('r')

# Example usage
if __name__ == "__main__":
    print(f"Got {len(nouns)} nouns, {len(adjectives)} adjectives, and {len(adverbs)} adverbs.")
    #print("Sample noun:", nouns[:5])
    #print("Sample adjective:", adjectives[:5])
    #print("Sample adverb:", adverbs[:5])
    print(f"I invite you to consider a new name: {random.choice(adverbs)} {random.choice(adjectives)} {random.choice(nouns)}")