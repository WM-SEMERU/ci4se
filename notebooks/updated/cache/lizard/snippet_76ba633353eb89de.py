def log(x, base=None):
    if base == 10:
        return np.log10(x)
    elif base == 2:
        return np.log2(x)
    elif base is None or base == np.e:
        return np.log(x)
    else:
        return np.log(x) / np.log(base)