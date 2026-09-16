def effective_n(x):
    if np.shape(x) < (2,):
        raise ValueError(
            'Calculation of effective sample size requires multiple chains of the same length.'
            )
    try:
        m, n = np.shape(x)
    except ValueError:
        return [effective_n(np.transpose(y)) for y in np.transpose(x)]
    s2 = gelman_rubin(x, return_var=True)
    negative_autocorr = False
    t = 1
    variogram = lambda t: sum(sum((x[j][i] - x[j][i - t]) ** 2 for i in
        range(t, n)) for j in range(m)) / (m * (n - t))
    rho = np.ones(n)
    while not negative_autocorr and t < n:
        rho[t] = 1.0 - variogram(t) / (2.0 * s2)
        if not t % 2:
            negative_autocorr = sum(rho[t - 1:t + 1]) < 0
        t += 1
    return int(m * n / (1 + 2 * rho[1:t].sum()))