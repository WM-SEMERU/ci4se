def to_dict(self):
    d = {}
    for word, idx in self.vocab.iteritems():
        d[word] = self.array[idx].tolist()
    return d