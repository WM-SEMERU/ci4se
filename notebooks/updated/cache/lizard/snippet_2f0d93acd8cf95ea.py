def previous(self, day_of_week=None):
    if day_of_week is None:
        day_of_week = self.day_of_week
    if day_of_week < SUNDAY or day_of_week > SATURDAY:
        raise ValueError('Invalid day of week')
    dt = self.subtract(days=1)
    while dt.day_of_week != day_of_week:
        dt = dt.subtract(days=1)
    return dt