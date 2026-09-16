def _GetNormalizedTimestamp(self):
    if self._normalized_timestamp is None:
        if self._timestamp is not None:
            self._normalized_timestamp = decimal.Decimal(self._timestamp
                ) / definitions.MILLISECONDS_PER_SECOND
    return self._normalized_timestamp