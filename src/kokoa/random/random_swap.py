import random

def random_swap(sentence: str, n: int=1, keep_origin: bool=True) -> dict:
    """Randomly swap two words in the sentence n times."""
    words = sentence.split()
    length = len(words)

    for _ in range(n):
        idx1, idx2 = random.sample(range(length), 2)
        words[idx1], words[idx2] = words[idx2], words[idx1]
    
    if keep_origin:
        result = {
            'original': sentence,
            'modified': ' '.join(words)
        }
    else:
        result = {
            'modified': ' '.join(words)
        }
    
    return result