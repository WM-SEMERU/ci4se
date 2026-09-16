def broadcast_transaction(self, hex_tx):
    resp = self.obj.sendrawtransaction(hex_tx)
    if len(resp) > 0:
        return {'transaction_hash': resp, 'success': True}
    else:
        return error_reply('Invalid response from bitcoind.')