def integralByInterval(requestContext, seriesList, intervalUnit):
    intervalDuration = int(to_seconds(parseTimeOffset(intervalUnit)))
    startTime = int(epoch(requestContext['startTime']))
    results = []
    for series in seriesList:
        newValues = []
        currentTime = series.start
        current = 0.0
        for val in series:
            if (currentTime - startTime) // intervalDuration != (
                currentTime - startTime - series.step) // intervalDuration:
                current = 0.0
            if val is None:
                newValues.append(current)
            else:
                current += val
                newValues.append(current)
            currentTime += series.step
        newName = "integralByInterval(%s,'%s')" % (series.name, intervalUnit)
        newSeries = TimeSeries(newName, series.start, series.end, series.
            step, newValues)
        newSeries.pathExpression = newName
        results.append(newSeries)
    return results