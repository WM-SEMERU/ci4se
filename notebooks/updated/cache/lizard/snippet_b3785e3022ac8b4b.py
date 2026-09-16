def list_markets_by_currency(self, currency):
    return [market['MarketName'] for market in self.get_markets()['result'] if
        market['MarketName'].lower().endswith(currency.lower())]