def get_deposit_address(self, currency):
    self._validate_currency(currency)
    self._log('get deposit address for {}'.format(currency))
    coin_name = self.major_currencies[currency]
    return self._rest_client.post(endpoint='/{}_deposit_address'.format(
        coin_name))