import random

def random_deletion(sentence, p=0.1, keep_origin=True):
    """Randomly delete words from the sentence with a probability p."""
    words = sentence.split()

    new_words = [word for word in words if random.random() > p]
    if len(new_words) == 0:
        new_words = words
    
    result = {
        'original': sentence,
        'modified': ' '.join(new_words)
    }
    return result if keep_origin else result['modified']