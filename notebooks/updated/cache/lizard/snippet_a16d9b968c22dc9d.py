def map_series(self, fn, dt_index=None):
    if dt_index == None:
        dt_index = self.index()
    return TimeSeriesRDD(dt_index, self.map(fn))