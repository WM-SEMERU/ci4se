def new_bg(self, bg):
    counts = []
    for pos in self.logP:
        D = {}
        for L, lp in pos.items():
            D[L] = math.pow(2.0, lp)
        counts.append(D)
    self.background = bg
    self.compute_from_counts(counts, 0)