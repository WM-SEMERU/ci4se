def get_symbol_info(self, symbol):
    res = self._get('exchangeInfo')
    for item in res['symbols']:
        if item['symbol'] == symbol.upper():
            return item
    return None