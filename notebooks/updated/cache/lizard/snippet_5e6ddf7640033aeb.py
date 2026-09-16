def get_dividendhistory(self, symbol, startDate, endDate, items=None):
    startDate, endDate = self.__get_time_range(startDate, endDate)
    response = self.select('yahoo.finance.dividendhistory', items).where([
        'symbol', '=', symbol], ['startDate', '=', startDate], ['endDate',
        '=', endDate])
    return response