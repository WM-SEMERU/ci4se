def _nth_of_year(self, nth, day_of_week):
    if nth == 1:
        return self.first_of('year', day_of_week)
    dt = self.first_of('year')
    year = dt.year
    for i in range(nth - (1 if dt.day_of_week == day_of_week else 0)):
        dt = dt.next(day_of_week)
    if year != dt.year:
        return False
    return self.on(self.year, dt.month, dt.day).start_of('day')