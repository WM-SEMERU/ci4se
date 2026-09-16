def batch_means(x, f=lambda y: y, theta=0.5, q=0.95, burn=0):
    try:
        import scipy
        from scipy import stats
    except ImportError:
        raise ImportError('SciPy must be installed to use batch_means.')
    x = x[burn:]
    n = len(x)
    b = np.int(n ** theta)
    a = n / b
    t_quant = stats.t.isf(1 - q, a - 1)
    Y = np.array([np.mean(f(x[i * b:(i + 1) * b])) for i in xrange(a)])
    sig = b / (a - 1.0) * sum((Y - np.mean(f(x))) ** 2)
    return t_quant * sig / np.sqrt(n)