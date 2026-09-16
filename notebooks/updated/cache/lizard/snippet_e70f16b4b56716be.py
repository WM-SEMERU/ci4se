def _calc_q_h0(n, x, h, nt, n_jobs=1, verbose=0, random_state=None):
    rng = check_random_state(random_state)
    par, func = parallel_loop(_calc_q_statistic, n_jobs, verbose)
    q = par(func(rng.permutation(x.T).T, h, nt) for _ in range(n))
    return np.array(q)