def degrees(x):
    if isinstance(x, UncertainFunction):
        mcpts = np.degrees(x._mcpts)
        return UncertainFunction(mcpts)
    else:
        return np.degrees(x)