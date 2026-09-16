def min_rank(series, ascending=True):
    ranks = series.rank(method='min', ascending=ascending)
    return ranks