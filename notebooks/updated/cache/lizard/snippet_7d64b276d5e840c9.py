def krai_to_raw(self, amount):
    amount = self._process_value(amount, 'int')
    payload = {'amount': amount}
    resp = self.call('krai_to_raw', payload)
    return int(resp['amount'])