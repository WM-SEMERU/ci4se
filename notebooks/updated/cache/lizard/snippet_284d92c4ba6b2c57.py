def humidity_series(self):
    return [(tstamp, self._station_history.get_measurements()[tstamp][
        'humidity']) for tstamp in self._station_history.get_measurements()]