def _remove_zeros(votes, fpl, cl, ranking):
    for v in votes:
        for r in v:
            if r not in fpl:
                v.remove(r)
    for c in cl:
        if c not in fpl:
            if c not in ranking:
                ranking.append((c, 0))