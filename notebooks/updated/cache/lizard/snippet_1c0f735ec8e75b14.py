def update(self, truth, guess, features):

    def upd_feat(c, f, w, v):
        param = f, c
        self._totals[param] += (self.i - self._tstamps[param]) * w
        self._tstamps[param] = self.i
        self.weights[f][c] = w + v
    self.i += 1
    if truth == guess:
        return None
    for f in features:
        weights = self.weights.setdefault(f, {})
        upd_feat(truth, f, weights.get(truth, 0.0), 1.0)
        upd_feat(guess, f, weights.get(guess, 0.0), -1.0)
    return None