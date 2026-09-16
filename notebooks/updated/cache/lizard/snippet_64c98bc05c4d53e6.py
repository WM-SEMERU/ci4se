def CopyToDateTimeString(self):
    if self._timestamp is None:
        return None
    number_of_days, hours, minutes, seconds = self._GetTimeValues(int(self.
        _timestamp))
    year, month, day_of_month = self._GetDateValuesWithEpoch(number_of_days,
        self._EPOCH)
    microseconds = int(self._timestamp % 1 * definitions.
        MICROSECONDS_PER_SECOND)
    return '{0:04d}-{1:02d}-{2:02d} {3:02d}:{4:02d}:{5:02d}.{6:06d}'.format(
        year, month, day_of_month, hours, minutes, seconds, microseconds)