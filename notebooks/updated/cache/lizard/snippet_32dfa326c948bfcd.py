def log10(x):
    if isinstance(x, UncertainFunction):
        mcpts = np.log10(x._mcpts)
        return UncertainFunction(mcpts)
    else:
        return np.log10(x)