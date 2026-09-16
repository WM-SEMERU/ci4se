def on_state_changed(self, previous_state, new_state):
    _logger.info(
        'Message receiver %r state changed from %r to %r on connection: %r',
        self.name, previous_state, new_state, self._session._connection.
        container_id)
    self._state = new_state