def nb_ll_row(params, data_row):
    p = params[0]
    r = params[1]
    n = len(data_row)
    ll = np.sum(gammaln(data_row + r)) - np.sum(gammaln(data_row + 1))
    ll -= n * gammaln(r)
    ll += np.sum(data_row) * np.log(p)
    ll += n * r * np.log(1 - p)
    return -ll