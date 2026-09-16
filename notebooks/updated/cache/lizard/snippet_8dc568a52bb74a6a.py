def save(self, fname):
    vec = self.vectors
    voc = self.vocabulary.getstate()
    state = voc, vec
    with open(fname, 'wb') as f:
        pickle.dump(state, f, protocol=pickle.HIGHEST_PROTOCOL)