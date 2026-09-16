def logSE(x1, x2=-1):
    e = get_valid_error(x1, x2)
    return 10 * np.log10(e ** 2)