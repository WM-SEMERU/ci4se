def emit(self, prob_min=0.0, prob_max=1.0):
    if not self.cumP:
        for logcol in self.logP:
            tups = []
            for L in ACGT:
                p = math.pow(2, logcol[L])
                tups.append((p, L))
            tups.sort()
            cumu = []
            tot = 0
            for p, L in tups:
                tot = tot + p
                cumu.append((tot, L))
            self.cumP.append(cumu)
    s = []
    u = (prob_max - prob_min) * random() + prob_min
    for cumu in self.cumP:
        last = 0
        for p, L in cumu:
            if last < u and u <= p:
                letter = L
                break
            else:
                last = p
        s.append(L)
    return ''.join(s)