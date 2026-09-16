def _find_position_of_minute(self, minute_dt):
    return find_position_of_minute(self._market_open_values, self.
        _market_close_values, minute_dt.value / NANOS_IN_MINUTE, self.
        _minutes_per_day, False)