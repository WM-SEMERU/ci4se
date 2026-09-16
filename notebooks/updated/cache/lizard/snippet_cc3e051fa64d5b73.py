def commit(self):
    self._tx_active = False
    return self._channel.rpc_request(specification.Tx.Commit())