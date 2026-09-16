def rate_limits(self):
    if not self._rate_limits:
        self._rate_limits = utilities.get_rate_limits(self._response)
    return self._rate_limits