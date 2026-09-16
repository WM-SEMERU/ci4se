def freedman_diaconis_bins(a):
    a = np.asarray(a)
    h = 2 * iqr(a) / len(a) ** (1 / 3)
    if h == 0:
        bins = np.ceil(np.sqrt(a.size))
    else:
        bins = np.ceil((np.nanmax(a) - np.nanmin(a)) / h)
    return np.int(bins)