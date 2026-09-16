def clean(self, force: bool=False):
    with (yield from self._lock):
        for connection in tuple(self.ready):
            if force or connection.closed():
                connection.close()
                self.ready.remove(connection)