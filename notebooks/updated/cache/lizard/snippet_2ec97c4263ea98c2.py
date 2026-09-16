def close_idle_connections(self, pool_id=None):
    if not hasattr(self, '_pools'):
        return
    if pool_id:
        if pool_id not in self._pools:
            raise ProgrammingError('pool %r does not exist' % pool_id)
        else:
            pool = self._pools[pool_id]
            pool.close()
    else:
        for pool_id, pool in self._pools.items():
            pool.close()