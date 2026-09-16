def mulpyplex(self, *stashes):
    return mulpyplexer.MP(list(itertools.chain.from_iterable(self._stashes[
        s] for s in stashes)))