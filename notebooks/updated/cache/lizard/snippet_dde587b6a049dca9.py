def can_receive_messages(self):
    with self.lock:
        return not self._state.is_waiting_for_start(
            ) and not self._state.is_connection_closed()