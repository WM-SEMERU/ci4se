def withdraw(self, currency, quantity, address, paymentid=None):
    options = {'currency': currency, 'quantity': quantity, 'address': address}
    if paymentid:
        options['paymentid'] = paymentid
    return self._api_query(path_dict={API_V1_1: '/account/withdraw',
        API_V2_0: '/key/balance/withdrawcurrency'}, options=options,
        protection=PROTECTION_PRV)