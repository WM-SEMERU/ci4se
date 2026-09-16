def summary(self, summary):
    if summary is not None and len(summary) > 25000:
        raise ValueError(
            'Invalid value for `summary`, length must be less than or equal to `25000`'
            )
    if summary is not None and len(summary) < 0:
        raise ValueError(
            'Invalid value for `summary`, length must be greater than or equal to `0`'
            )
    self._summary = summary