def register_listener(self, listener, reading=False):
    listener_id = hashable_identity(listener)
    self._listeners[listener_id] = listener, reading
    logger.debug('Register listener for {}'.format(self.name))