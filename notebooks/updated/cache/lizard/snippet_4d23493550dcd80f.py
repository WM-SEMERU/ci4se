def replace(self, year=None, week=None):
    return self.__class__(self.year if year is None else year, self.week if
        week is None else week)