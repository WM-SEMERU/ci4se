def sorted_timeseries(self, ascending=True):
    sortorder = 1
    if not ascending:
        sortorder = -1
    data = sorted(self._timeseriesData, key=lambda i: sortorder * i[0])
    newTS = TimeSeries(self._normalized)
    for entry in data:
        newTS.add_entry(*entry)
    newTS._sorted = ascending
    return newTS