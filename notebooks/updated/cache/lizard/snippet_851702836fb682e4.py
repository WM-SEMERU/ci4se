def most_frequent(self, k, inplace=False):
    vocabulary = self.vocabulary.most_frequent(k)
    vectors = np.asarray([self[w] for w in vocabulary])
    if inplace:
        self.vocabulary = vocabulary
        self.vectors = vectors
        return self
    return Embedding(vectors=vectors, vocabulary=vocabulary)