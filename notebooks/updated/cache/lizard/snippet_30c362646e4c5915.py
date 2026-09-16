def returnTradeHistory(self, currencyPair, start=None, end=None):
    return self._public('returnTradeHistory', currencyPair=currencyPair,
        start=start, end=end)