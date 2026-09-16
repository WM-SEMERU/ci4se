def ks_stat(data):
    samples = len(data)
    uniform = arange(0, samples + 1) / samples
    d_plus = (uniform[1:] - data).max()
    d_minus = (data - uniform[:-1]).max()
    return max(d_plus, d_minus)