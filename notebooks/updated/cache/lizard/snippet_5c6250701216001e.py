def query(self, query, time_precision='s', chunked=False):
    result = InfluxDBClient.query(self, query=query, time_precision=
        time_precision, chunked=chunked)
    if len(result) == 0:
        return result
    elif len(result) == 1:
        return self._to_dataframe(result[0], time_precision)
    else:
        ret = {}
        for time_series in result:
            ret[time_series['name']] = self._to_dataframe(time_series,
                time_precision)
        return ret