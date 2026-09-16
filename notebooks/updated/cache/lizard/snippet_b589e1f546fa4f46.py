def convert_to_btc_on(self, amount, currency, date_obj):
    if isinstance(amount, Decimal):
        use_decimal = True
    else:
        use_decimal = self._force_decimal
    start = date_obj.strftime('%Y-%m-%d')
    end = date_obj.strftime('%Y-%m-%d')
    url = (
        'https://api.coindesk.com/v1/bpi/historical/close.json?start={}&end={}&currency={}'
        .format(start, end, currency))
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        price = data.get('bpi', {}).get(start, None)
        if price:
            if use_decimal:
                price = Decimal(price)
            try:
                converted_btc = amount / price
                return converted_btc
            except TypeError:
                raise DecimalFloatMismatchError(
                    'convert_to_btc_on requires amount parameter is of type Decimal when force_decimal=True'
                    )
    raise RatesNotAvailableError(
        'BitCoin Rates Source Not Ready For Given Date')