def keepLastValue(requestContext, seriesList, limit=INF):
    for series in seriesList:
        series.name = 'keepLastValue(%s)' % series.name
        series.pathExpression = series.name
        consecutiveNones = 0
        for i, value in enumerate(series):
            series[i] = value
            if i == 0:
                continue
            if value is None:
                consecutiveNones += 1
            else:
                if 0 < consecutiveNones <= limit:
                    for index in range(i - consecutiveNones, i):
                        series[index] = series[i - consecutiveNones - 1]
                consecutiveNones = 0
        if 0 < consecutiveNones <= limit:
            for index in range(len(series) - consecutiveNones, len(series)):
                series[index] = series[len(series) - consecutiveNones - 1]
    return seriesList