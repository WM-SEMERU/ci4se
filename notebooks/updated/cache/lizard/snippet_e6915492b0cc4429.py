def add_entry(self, timestamp, data):
    self._normalized = self._predefinedNormalized
    self._sorted = self._predefinedSorted
    tsformat = self._timestampFormat
    if tsformat is not None:
        timestamp = TimeSeries.convert_timestamp_to_epoch(timestamp, tsformat)
    self._timeseriesData.append([float(timestamp), float(data)])