def execute(self, timeSeries):
    self._calculate_values_to_forecast(timeSeries)
    alpha = self._parameters['smoothingFactor']
    beta = self._parameters['trendSmoothingFactor']
    resultList = []
    estimator = None
    trend = None
    lastT = None
    append = resultList.append
    for idx in xrange(len(timeSeries)):
        t = timeSeries[idx]
        if estimator is None:
            estimator = t[1]
            lastT = t
            continue
        if 0 == len(resultList):
            append([t[0], estimator])
            trend = t[1] - lastT[1]
            lastT = t
            lastEstimator = estimator
            continue
        estimator = alpha * t[1] + (1 - alpha) * (estimator + trend)
        trend = beta * (estimator - lastEstimator) + (1 - beta) * trend
        append([t[0], estimator])
        lastT = t
        lastEstimator = estimator
    if self._parameters['valuesToForecast'] > 0:
        currentTime = resultList[-1][0]
        normalizedTimeDiff = currentTime - resultList[-2][0]
        for idx in xrange(1, self._parameters['valuesToForecast'] + 1):
            currentTime += normalizedTimeDiff
            forecast = estimator + idx * trend
            append([currentTime, forecast])
    return TimeSeries.from_twodim_list(resultList)