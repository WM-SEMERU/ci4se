def exclude_time(self, start, end, days):
    self._excluded_times.append(TimeRange(start, end, days))
    return self