def _start_of_week(self):
    dt = self
    if self.day_of_week != pendulum._WEEK_STARTS_AT:
        dt = self.previous(pendulum._WEEK_STARTS_AT)
    return dt.start_of('day')