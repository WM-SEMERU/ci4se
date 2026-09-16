def add_inputs(self, rawtx, wifs, change_address=None, fee=10000, dont_sign
    =False):
    tx = deserialize.tx(rawtx)
    keys = deserialize.keys(self.testnet, wifs)
    fee = deserialize.positive_integer(fee)
    if change_address is not None:
        change_address = deserialize.address(self.testnet, change_address)
    tx = control.add_inputs(self.service, self.testnet, tx, keys,
        change_address=change_address, fee=fee)
    if not dont_sign:
        tx = control.sign_tx(self.service, self.testnet, tx, keys)
    return serialize.tx(tx)