def get_unspents(self, address):
    addresses = []
    addresses.append(str(address))
    min_confirmations = 0
    max_confirmation = 2000000000
    unspents = self.obj.listunspent(min_confirmations, max_confirmation,
        addresses)
    return self.format_unspents(unspents)