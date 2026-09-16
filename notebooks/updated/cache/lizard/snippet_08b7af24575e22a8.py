def kde(data, grid, package, **kwargs):
    if package == 'statsmodels':
        package = 'statsmodels-m'
    func = KDE_FUNCS[package]
    return func(data, grid, **kwargs)