def _invariant(self, rank, n):
    minimum = n + 1
    for i in self._invariants:
        delta = i._delta(rank, n)
        if delta < minimum:
            minimum = delta
    return math.floor(minimum)