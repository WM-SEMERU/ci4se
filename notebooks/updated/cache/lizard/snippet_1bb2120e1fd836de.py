async def release(self, connection, *, timeout=None):
    if type(connection
        ) is not PoolConnectionProxy or connection._holder._pool is not self:
        raise exceptions.InterfaceError(
            'Pool.release() received invalid connection: {connection!r} is not a member of this pool'
            .format(connection=connection))
    if connection._con is None:
        return
    self._check_init()
    connection._con._on_release()
    ch = connection._holder
    if timeout is None:
        timeout = ch._timeout
    return await asyncio.shield(ch.release(timeout), loop=self._loop)