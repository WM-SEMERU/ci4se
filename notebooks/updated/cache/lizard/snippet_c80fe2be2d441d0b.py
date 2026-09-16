def add_log_listener(self, callback):
    if self.is_closed():
        raise exceptions.InterfaceError('connection is closed')
    self._log_listeners.add(callback)