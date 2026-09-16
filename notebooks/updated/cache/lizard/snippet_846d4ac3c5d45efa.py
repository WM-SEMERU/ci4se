def input_sender(self):
    if self._input_sender is None and self._sender_id:
        try:
            self._input_sender = self._client.session.get_input_entity(self
                ._sender_id)
        except ValueError:
            pass
    return self._input_sender