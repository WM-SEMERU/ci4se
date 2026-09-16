def get_month(self):
    year = super(BuildableDayArchiveView, self).get_year()
    month = super(BuildableDayArchiveView, self).get_month()
    fmt = self.get_month_format()
    dt = date(int(year), int(month), 1)
    return dt.strftime(fmt)