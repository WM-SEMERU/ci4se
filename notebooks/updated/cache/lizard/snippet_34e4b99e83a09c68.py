def any_to_datetime(self, time_input, tz=None):
    dt_value = self.unix_time_to_datetime(time_input, tz)
    if dt_value is None:
        dt_value = self.date_to_datetime(time_input, tz)
    if dt_value is None:
        dt_value = self.human_date_to_datetime(time_input, tz)
    if dt_value is None:
        raise RuntimeError('Could not format input ({}) to datetime string.'
            .format(time_input))
    return dt_value