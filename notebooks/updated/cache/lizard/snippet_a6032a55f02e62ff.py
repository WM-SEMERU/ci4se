def acquire(self):
    self._condition.acquire()
    try:
        if self._maxsize is not None and self._block:
            while not self._pool and self._nconnections == self._maxsize:
                self._condition.wait(timeout=None)
        while self._pool:
            pooledconn = self._pool.pop(0)
            if (self._idlettl is not None and pooledconn.released + self.
                _idlettl < time.time()):
                pooledconn.connection.close()
                self._nconnections -= 1
            else:
                return pooledconn.connection
        connection = self._dbapi2.connect(*(), **self._connection_args.copy())
        self._nconnections += 1
        return connection
    finally:
        self._condition.release()