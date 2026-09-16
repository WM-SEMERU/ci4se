def add_series(self, series):
    if not isinstance(series, Series):
        raise TypeError("'%s' is not a Series" % str(series))
    self._all_series.append(series)
    series._chart = self