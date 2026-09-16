def tokprob(self, tok, nonT):
    p = self._T.get(tok, 0) / float(self._T.get(nonT, 1))
    if not p:
        p = MIN_PROB
    return p