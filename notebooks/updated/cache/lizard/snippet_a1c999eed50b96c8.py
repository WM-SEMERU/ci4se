def get_broadcast_message(self, rawtx):
    tx = deserialize.tx(rawtx)
    result = control.get_broadcast_message(self.testnet, tx)
    result['signature'] = serialize.signature(result['signature'])
    return result