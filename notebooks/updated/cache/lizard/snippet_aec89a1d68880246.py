def _GetDaysPerMonth(self, year, month):
    if month not in range(1, 13):
        raise ValueError('Month value out of bounds.')
    days_per_month = self._DAYS_PER_MONTH[month - 1]
    if month == 2 and self._IsLeapYear(year):
        days_per_month += 1
    return days_per_month