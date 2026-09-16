def bestscan(self, seq):
    matches, endpoints, scores = self.scan(seq, -100)
    if not scores:
        return -100
    scores.sort()
    best = scores[-1]
    return best