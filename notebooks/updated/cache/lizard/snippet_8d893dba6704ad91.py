def time_series_rdd_from_pandas_series_rdd(series_rdd):
    first = series_rdd.first()
    dt_index = irregular(first[1].index, series_rdd.ctx)
    return TimeSeriesRDD(dt_index, series_rdd.mapValues(lambda x: x.values))