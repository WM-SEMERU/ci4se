def get_ticker(self):
    lastQuote = self.data['quote'][-1]
    lastTrade = self.data['trade'][-1]
    ticker = {'last': lastTrade['price'], 'buy': lastQuote['bidPrice'],
        'sell': lastQuote['askPrice'], 'mid': (float(lastQuote['bidPrice'] or
        0) + float(lastQuote['askPrice'] or 0)) / 2}
    instrument = self.data['instrument'][0]
    return {k: round(float(v or 0), instrument['tickLog']) for k, v in list
        (ticker.items())}