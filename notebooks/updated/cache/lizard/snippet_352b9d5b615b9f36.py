def daterange(self, datecol, date_start, op, **args):
    df = self._daterange(datecol, date_start, op, **args)
    if df is None:
        self.err('Can not select date range data')
    self.df = df