def get_victoria_day(self, year):
    may_24th = date(year, 5, 24)
    shift = may_24th.weekday() or 7
    victoria_day = may_24th - timedelta(days=shift)
    return victoria_day, 'Victoria Day'