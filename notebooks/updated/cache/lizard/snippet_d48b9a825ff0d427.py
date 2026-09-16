def generate_params(n_items, interval=5.0, ordered=False):
    r
    params = np.random.uniform(low=0, high=interval, size=n_items)
    if ordered:
        params.sort()
    return params - params.mean()