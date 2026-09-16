def pareto_nbd_model(T, r, alpha, s, beta, size=1):
    if type(T) in [float, int]:
        T = T * np.ones(size)
    else:
        T = np.asarray(T)
    lambda_ = random.gamma(r, scale=1.0 / alpha, size=size)
    mus = random.gamma(s, scale=1.0 / beta, size=size)
    columns = ['frequency', 'recency', 'T', 'lambda', 'mu', 'alive',
        'customer_id']
    df = pd.DataFrame(np.zeros((size, len(columns))), columns=columns)
    for i in range(size):
        l = lambda_[i]
        mu = mus[i]
        time_of_death = random.exponential(scale=1.0 / mu)
        times = []
        next_purchase_in = random.exponential(scale=1.0 / l)
        while np.sum(times) + next_purchase_in < min(time_of_death, T[i]):
            times.append(next_purchase_in)
            next_purchase_in = random.exponential(scale=1.0 / l)
        times = np.array(times).cumsum()
        df.iloc[i] = np.unique(np.array(times).astype(int)).shape[0], np.max(
            times if times.shape[0] > 0 else 0), T[i
            ], l, mu, time_of_death > T[i], i
    return df.set_index('customer_id')