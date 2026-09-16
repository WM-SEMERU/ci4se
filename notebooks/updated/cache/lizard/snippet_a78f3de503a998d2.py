def payment(self, origin, destination, amount):
    if type(amount) != Decimal:
        amount = Decimal(amount)
    if amount <= 0:
        raise Exception('Amount must be a positive number')
    all_addresses = []
    accounts = self.listaccounts()
    if origin in accounts:
        if destination in accounts:
            with self.openwallet():
                result = self.move(origin, destination, amount)
            return self.record_tx(origin, None, amount, result, destination)
        for account in accounts:
            addresses = self.getaddressesbyaccount(account)
            if destination in addresses:
                with self.openwallet():
                    result = self.move(origin, account, amount)
                return self.record_tx(origin, destination, amount, result,
                    account)
        else:
            with self.openwallet():
                txhash = self.sendfrom(origin, destination, amount)
            return self.record_tx(origin, destination, amount, txhash)