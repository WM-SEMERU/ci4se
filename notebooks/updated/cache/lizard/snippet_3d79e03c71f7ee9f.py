def mcc(x, axis=0, autocorrect=False):
    if axis is not 0:
        x = x.T
    n, c = x.shape
    if c < 2:
        raise Exception('Only ' + str(c) +
            ' variables provided. Min. 2 required.')
    r = np.ones((c, c))
    p = np.zeros((c, c))
    for i in range(0, c):
        for j in range(i + 1, c):
            cm = confusion(x[:, (i)], x[:, (j)])
            r[i, j] = confusion_to_mcc(cm)
            r[j, i] = r[i, j]
            p[i, j] = 1 - scipy.stats.chi2.cdf(r[i, j] * r[i, j] * n, 1)
            p[j, i] = p[i, j]
    if autocorrect:
        r = np.nan_to_num(r)
    return r, p