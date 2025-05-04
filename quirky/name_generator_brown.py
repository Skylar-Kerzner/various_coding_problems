import subprocess
import sys
import random

# Install nltk if needed
try:
    import nltk
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "nltk"])
    import nltk

import random
from collections import Counter

# Download once
nltk.download('brown')
nltk.download('averaged_perceptron_tagger')

from nltk.corpus import brown

# Get words and their POS tags
words = brown.words()
tagged_words = nltk.pos_tag(words)

# Count by POS
pos_counts = Counter(tag for word, tag in tagged_words)

# Collect frequent words by simplified POS
def get_common_words(pos_prefix, top_n=500):
    filtered = [word.lower() for word, tag in tagged_words
                if tag.startswith(pos_prefix) and word.isalpha()]
    common = Counter(filtered).most_common(top_n)
    return [word for word, _ in common]

# Get top 500 of each
common_nouns = get_common_words('NN', 500)
common_adjectives = get_common_words('JJ', 500)
common_adverbs = get_common_words('RB', 500)

# Preview
print("Nouns:", common_nouns[:10])
print("Adjectives:", common_adjectives[:10])
print("Adverbs:", common_adverbs[:10])
print(f"I invite you to consider a new name: {random.choice(adverbs)} {random.choice(adjectives)} {random.choice(nouns)}")