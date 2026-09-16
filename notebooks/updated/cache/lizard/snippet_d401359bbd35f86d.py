def vote_random(candidates, votes, n_winners):
    rcands = list(candidates)
    shuffle(rcands)
    rcands = rcands[:min(n_winners, len(rcands))]
    best = [(i, 0.0) for i in rcands]
    return best