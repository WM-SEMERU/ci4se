def gday_of_year(self):
    return (self.date - dt.date(self.date.year, 1, 1)).days