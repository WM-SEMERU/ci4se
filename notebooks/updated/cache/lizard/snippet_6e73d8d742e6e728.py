def lsr_rankings(n_items, data, alpha=0.0, initial_params=None):
    weights, chain = _init_lsr(n_items, alpha, initial_params)
    for ranking in data:
        sum_ = weights.take(ranking).sum()
        for i, winner in enumerate(ranking[:-1]):
            val = 1.0 / sum_
            for loser in ranking[i + 1:]:
                chain[loser, winner] += val
            sum_ -= weights[winner]
    chain -= np.diag(chain.sum(axis=1))
    return log_transform(statdist(chain))