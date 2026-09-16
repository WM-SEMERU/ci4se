def is_within_limits(self, limit, date, dates):
    return any(self.second_diff(date, d) <= limit for d in dates)