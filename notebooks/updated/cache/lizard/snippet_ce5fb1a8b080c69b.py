def optimization_loop(self, timeSeries, forecastingMethod,
    remainingParameters, currentParameterValues=None):
    if currentParameterValues is None:
        currentParameterValues = {}
    if 0 == len(remainingParameters):
        for parameter in currentParameterValues:
            forecastingMethod.set_parameter(parameter,
                currentParameterValues[parameter])
        forecast = timeSeries.apply(forecastingMethod)
        error = self._errorClass(**self._errorMeasureKWArgs)
        if not error.initialize(timeSeries, forecast):
            return []
        return [[error, dict(currentParameterValues)]]
    localParameter = remainingParameters[-1]
    localParameterName = localParameter[0]
    localParameterValues = localParameter[1]
    results = []
    for value in localParameterValues:
        currentParameterValues[localParameterName] = value
        remainingParameters = remainingParameters[:-1]
        results += self.optimization_loop(timeSeries, forecastingMethod,
            remainingParameters, currentParameterValues)
    return results