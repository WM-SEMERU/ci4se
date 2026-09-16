def add_entry(self, timestamp, data):
    if not isinstance(data, list):
        data = [data]
    if len(data) != self._dimensionCount:
        raise ValueError(
            'data does contain %s instead of %s dimensions.\n   %s' % (len(
            data), self._dimensionCount, data))
    self._normalized = self._predefinedNormalized
    self._sorted = self._predefinedSorted
    tsformat = self._timestampFormat
    if tsformat is not None:
        timestamp = TimeSeries.convert_timestamp_to_epoch(timestamp, tsformat)
    self._timeseriesData.append([float(timestamp)] + [float(dimensionValue) for
        dimensionValue in data])