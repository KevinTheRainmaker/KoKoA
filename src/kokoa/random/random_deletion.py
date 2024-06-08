import random

def random_deletion(sentence: str, p: float=0.1, keep_origin: bool=True) -> dict:
    """Randomly delete words from the sentence with a probability p."""
    words = sentence.split()

    new_words = [word for word in words if random.random() > p]
    if len(new_words) == 0:
        new_words = words
    
    if keep_origin:
        result = {
            'original': sentence,
            'modified': ' '.join(new_words)
        }
    else:
        result = {
            'modified': ' '.join(new_words)
        }
    
    return result