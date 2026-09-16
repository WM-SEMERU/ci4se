def circ_corrcc(x, y, tail='two-sided'):
    from scipy.stats import norm
    x = np.asarray(x)
    y = np.asarray(y)
    if x.size != y.size:
        raise ValueError('x and y must have the same length.')
    x, y = remove_na(x, y, paired=True)
    n = x.size
    x_sin = np.sin(x - circmean(x))
    y_sin = np.sin(y - circmean(y))
    r = np.sum(x_sin * y_sin) / np.sqrt(np.sum(x_sin ** 2) * np.sum(y_sin ** 2)
        )
    tval = np.sqrt(n * (x_sin ** 2).mean() * (y_sin ** 2).mean() / np.mean(
        x_sin ** 2 * y_sin ** 2)) * r
    pval = 2 * norm.sf(abs(tval))
    pval = pval / 2 if tail == 'one-sided' else pval
    return np.round(r, 3), pval