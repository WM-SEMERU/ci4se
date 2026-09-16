def geweke(x, first=0.1, last=0.5, intervals=20, maxlag=20):
    if not has_sm:
        print(
            'statsmodels not available. Geweke diagnostic cannot be calculated.'
            )
        return
    if np.ndim(x) > 1:
        return [geweke(y, first, last, intervals) for y in np.transpose(x)]
    if first + last >= 1:
        raise ValueError('Invalid intervals for Geweke convergence analysis',
            (first, last))
    zscores = [None] * intervals
    starts = np.linspace(0, int(len(x) * (1.0 - last)), intervals).astype(int)
    for i, s in enumerate(starts):
        x_trunc = x[s:]
        n = len(x_trunc)
        first_slice = x_trunc[:int(first * n)]
        last_slice = x_trunc[int(last * n):]
        z = first_slice.mean() - last_slice.mean()
        z /= np.sqrt(spec(first_slice) / len(first_slice) + spec(last_slice
            ) / len(last_slice))
        zscores[i] = len(x) - n, z
    return zscores