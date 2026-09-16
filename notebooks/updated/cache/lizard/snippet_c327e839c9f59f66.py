def init_poolmanager(self, connections, maxsize, block=DEFAULT_POOLBLOCK,
    **pool_kwargs):
    self._pool_connections = connections
    self._pool_maxsize = maxsize
    self._pool_block = block
    self.poolmanager = PoolManager(num_pools=connections, maxsize=maxsize,
        block=block, strict=True, **pool_kwargs)