def FromTimedelta(self, td):
    self._NormalizeDuration(td.seconds + td.days * _SECONDS_PER_DAY, td.
        microseconds * _NANOS_PER_MICROSECOND)