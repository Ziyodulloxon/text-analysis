import math
import re


def map_frequency(words):
    word_map = {}
    for word in words:
        if word in word_map:
            word_map[word] += 1
        else:
            word_map[word] = 1
    return word_map

def word_filter(word: str):
    match = re.search(r'[a-z0-9.-]+', word)
    return match.group()

def tf_idf_map(text: str) -> list:
    tf = term_frequency(text)
    idf = inverse_document_frequency(text)
    result = []

    for word, fr in tf.items():
        result.append({
            "word": word,
            "tf": round(fr, 2),
            "idf": round(idf[word], 2) if word in idf else 0
        })
    result = sorted(result, key=lambda w: w["idf"], reverse=True)
    return result[:50]


def inverse_document_frequency(text: str) -> dict:
    formatted = text.decode("utf-8").lower()
    words = list(set(formatted.split()))
    words = list(map(word_filter, words))
    documents = formatted.rsplit(". ")
    total = len(documents)
    frequency = {}
    result = {}
    for word in words:
        for doc in documents:
            if word in doc:
                frequency[word] = frequency[word] + 1 if word in frequency else 1

    for word, fr in frequency.items():
        print(word, " --> ", fr)
        result[word] = math.log(total / (fr + 1))
    return result


def term_frequency(text: str) -> dict:
    words = text.decode("utf-8").lower().split()
    words = list(map(word_filter, words))
    frequency = map_frequency(words)
    result = {}
    total = len(words)

    for word, fr in frequency.items():
        result[word] = fr / total

    return result
