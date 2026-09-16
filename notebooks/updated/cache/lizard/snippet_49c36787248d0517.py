def nonzero_monies(self):
    return [copy.copy(m) for m in self._money_obs if m.amount != 0]