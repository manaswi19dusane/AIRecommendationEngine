
from collections import Counter
import numpy as np

class SimpleVectorizer:

    def __init__(self):
        self.vocab = {}

    def fit_transform(self, texts):

        tokens = [t.lower().split() for t in texts]

        vocab = set()
        for t in tokens:
            vocab.update(t)

        self.vocab = {word: i for i, word in enumerate(vocab)}

        matrix = np.zeros((len(tokens), len(self.vocab)))

        for i, words in enumerate(tokens):
            counts = Counter(words)

            for word, count in counts.items():
                if word in self.vocab:
                    matrix[i][self.vocab[word]] = count

        return matrix
