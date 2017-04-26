import string

import nltk


CHARS_TO_IGNORE = string.punctuation + '–'


def tokenize(text):
    text = "".join([ch for ch in text if ch not in CHARS_TO_IGNORE])
    tokens = nltk.word_tokenize(text)
    return tokens