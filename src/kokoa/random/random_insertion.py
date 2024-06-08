import random

def random_insertion(sentence: str, p: float=0.1, keep_origin: bool=True) -> dict:
    """Randomly insert words from the sentence with a probability p."""
    words = sentence.split()
    new_words = words.copy()
    
    for _ in range(len(words)):
        if random.random() < p:
            insert_word = random.choice(words)
            insert_position = random.randint(0, len(new_words)-1)
            new_words.insert(insert_position, insert_word)
    
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