def _connect(self):
    future = concurrent.Future()
    try:
        connection = self._pool_manager.get(self.pid, self)
        self._connections[connection.fileno()] = connection
        future.set_result(connection)
        self._ioloop.add_handler(connection.fileno(), self._on_io_events,
            ioloop.IOLoop.WRITE)
    except pool.NoIdleConnectionsError:
        self._create_connection(future)
    return future