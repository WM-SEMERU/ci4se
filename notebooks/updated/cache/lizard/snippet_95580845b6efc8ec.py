def length(self, chain=-1):
    if chain is not None:
        if chain < 0:
            chain = range(self.db.chains)[chain]
        return self._trace[chain].shape[0]
    else:
        return sum([t.shape[0] for t in self._trace.values()])