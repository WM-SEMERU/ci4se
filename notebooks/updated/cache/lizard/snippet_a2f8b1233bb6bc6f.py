def transaction(self, tx_hash):
    endpoint = '/transactions/{tx_hash}'.format(tx_hash=tx_hash)
    return self.query(endpoint)