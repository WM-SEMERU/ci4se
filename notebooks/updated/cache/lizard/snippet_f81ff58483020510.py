def from_year(cls, year):
    first_day = date(year, 1, 1)
    return cls.from_date(first_day, period='year')