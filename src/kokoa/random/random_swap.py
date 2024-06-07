import random

def random_swap(sentence, n=1, keep_origin=True):
    """Randomly swap two words in the sentence n times."""
    words = sentence.split()
    length = len(words)

    for _ in range(n):
        idx1, idx2 = random.sample(range(length), 2)
        words[idx1], words[idx2] = words[idx2], words[idx1]
    
    result = {
        'original': sentence,
        'modified': ' '.join(words)
    }
    return result if keep_origin else result['modified']