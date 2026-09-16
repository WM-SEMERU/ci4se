def absolute(requestContext, seriesList):
    for series in seriesList:
        series.name = 'absolute(%s)' % series.name
        series.pathExpression = series.name
        for i, value in enumerate(series):
            series[i] = safeAbs(value)
    return seriesList