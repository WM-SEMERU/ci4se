def add_to_queue(self, series):
    result = self._android_api.add_to_queue(series_id=series.series_id)
    return result