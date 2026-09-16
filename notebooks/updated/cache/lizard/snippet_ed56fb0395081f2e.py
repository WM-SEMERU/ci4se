def get_parameters_at_instant(self, instant):
    if isinstance(instant, periods.Period):
        instant = instant.start
    elif isinstance(instant, (str, int)):
        instant = periods.instant(instant)
    else:
        assert isinstance(instant, periods.Instant
            ), 'Expected an Instant (e.g. Instant((2017, 1, 1)) ). Got: {}.'.format(
            instant)
    parameters_at_instant = self._parameters_at_instant_cache.get(instant)
    if parameters_at_instant is None and self.parameters is not None:
        parameters_at_instant = self.parameters.get_at_instant(str(instant))
        self._parameters_at_instant_cache[instant] = parameters_at_instant
    return parameters_at_instant