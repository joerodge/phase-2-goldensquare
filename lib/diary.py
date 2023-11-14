def make_snippet(text):
    words = text.split()
    if len(words) <= 5:
        return text

    # remove punctuation from last work apart from inverted commas
    five_words = ' '.join(words[:5]).strip(',.?;:') 
    return five_words + '...'

def count_words(text):
    return len(text.split())
