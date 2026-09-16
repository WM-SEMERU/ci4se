def split_utxos(self, wif, limit, fee=10000, max_outputs=100):
    key = deserialize.key(self.testnet, wif)
    limit = deserialize.positive_integer(limit)
    fee = deserialize.positive_integer(fee)
    max_outputs = deserialize.positive_integer(max_outputs)
    spendables = control.retrieve_utxos(self.service, [key.address()])
    txids = control.split_utxos(self.service, self.testnet, key, spendables,
        limit, fee=fee, max_outputs=max_outputs, publish=not self.dryrun)
    return serialize.txids(txids)