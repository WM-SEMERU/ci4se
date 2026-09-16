def countSeries(requestContext, *seriesLists):
    if not seriesLists or not any(seriesLists):
        series = constantLine(requestContext, 0).pop()
        series.pathExpression = 'countSeries()'
    else:
        seriesList, start, end, step = normalize(seriesLists)
        name = 'countSeries(%s)' % formatPathExpressions(seriesList)
        values = (int(len(row)) for row in zip_longest(*seriesList))
        series = TimeSeries(name, start, end, step, values)
        series.pathExpression = name
    return [series]