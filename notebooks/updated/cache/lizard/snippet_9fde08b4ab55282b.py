def toy_rbf_1d(optimize=True, plot=True):
    try:
        import pods
    except ImportError:
        print(
            'pods unavailable, see https://github.com/sods/ods for example datasets'
            )
        return
    data = pods.datasets.toy_rbf_1d()
    m = GPy.models.GPRegression(data['X'], data['Y'])
    if optimize:
        m.optimize('bfgs')
    if plot:
        m.plot()
    return m