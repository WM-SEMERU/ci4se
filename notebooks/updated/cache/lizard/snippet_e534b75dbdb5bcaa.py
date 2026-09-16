def vote_best(candidates, votes, n_winners):
    best = [votes[0][0]]
    for v in votes[1:]:
        if v[0][1] > best[0][1]:
            best = [v[0]]
    return best