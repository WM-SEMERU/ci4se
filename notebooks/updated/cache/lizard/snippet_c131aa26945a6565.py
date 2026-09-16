def _generate_next_parameter_value(self, parameter, forecastingMethod):
    interval = forecastingMethod.get_interval(parameter)
    precision = 10 ** self._precison
    startValue = interval[0]
    endValue = interval[1]
    if not interval[2]:
        startValue += precision
    if interval[3]:
        endValue += precision
    while startValue < endValue:
        parameterValue = startValue
        yield parameterValue
        startValue += precision