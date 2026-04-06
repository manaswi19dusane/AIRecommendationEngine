from collections import Counter
import numpy as np
from scipy.sparse import lil_matrix  # ✅ sparse matrix

class SimpleVectorizer:

    def __init__(self):
        self.vocab = {}

    def fit_transform(self, texts):

        tokens = [t.lower().split() for t in texts]

        vocab = set()
        for t in tokens:
            vocab.update(t)

        self.vocab = {word: i for i, word in enumerate(vocab)}

        # Use sparse matrix to save memory
        matrix = lil_matrix((len(tokens), len(self.vocab)))

        for i, words in enumerate(tokens):
            counts = Counter(words)
            for word, count in counts.items():
                if word in self.vocab:
                    matrix[i, self.vocab[word]] = count

        return matrix