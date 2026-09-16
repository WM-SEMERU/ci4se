def eth_getBlockByHash(self, bhash, tx_objects=True):
    result = yield from self.rpc_call('eth_getBlockByHash', [bhash, tx_objects]
        )
    return result