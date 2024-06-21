import random
import pickle
import os

data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
with open(os.path.join(data_dir, 'wordnet.pickle'), 'rb') as f:
    wordnet_data = pickle.load(f)

def synonym_replacement(sentence, n):
    """Replace words in the sentence with their synonyms based on WordNet."""
    words = sentence.split()
    length = len(words)
    
    if n > length:
        n = length
    
    indices = random.sample(range(len(words)), n)
    new_words = words.copy()
    
    for idx in indices:
        synonyms = get_synonyms(words[idx])
        if synonyms:
            new_words[idx] = random.choice(synonyms)
    
    return ' '.join(new_words)

def get_synonyms(word):
    """Get synonyms for a word using WordNet."""
    synomyms = []
    try:
        for syn in wordnet_data[word]:
            for s in syn:
                synomyms.append(s)
    except:
        pass

    return synomyms
