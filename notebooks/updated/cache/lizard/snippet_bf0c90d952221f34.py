def get_previous_price(self, currency, date_obj):
    start = date_obj.strftime('%Y-%m-%d')
    end = date_obj.strftime('%Y-%m-%d')
    url = (
        'https://api.coindesk.com/v1/bpi/historical/close.json?start={}&end={}&currency={}'
        .format(start, end, currency))
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        price = data.get('bpi', {}).get(start, None)
        if self._force_decimal:
            return Decimal(price)
        return price
    raise RatesNotAvailableError(
        'BitCoin Rates Source Not Ready For Given date')