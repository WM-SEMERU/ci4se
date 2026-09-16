def kde_statsmodels_u(data, grid, **kwargs):
    kde = KDEUnivariate(data)
    kde.fit(**kwargs)
    return kde.evaluate(grid)