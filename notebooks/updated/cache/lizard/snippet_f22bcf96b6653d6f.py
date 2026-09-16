def _message_received(self, message):
    with self.lock:
        self._state.receive_message(message)
        for callable in chain(self._on_message_received, self._on_message):
            callable(message)