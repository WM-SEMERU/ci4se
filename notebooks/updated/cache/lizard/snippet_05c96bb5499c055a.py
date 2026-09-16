def tokenize(self, docs):
    if self.n_jobs == 1:
        return [self._tokenize(doc) for doc in docs]
    else:
        return parallel(self._tokenize, docs, self.n_jobs)