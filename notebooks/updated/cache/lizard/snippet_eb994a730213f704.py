def execute(self, command, *args, **kwargs):
    if self.closed:
        raise PoolClosedError('Sentinel pool is closed')
    for pool in self._pools:
        return pool.execute(command, *args, **kwargs)