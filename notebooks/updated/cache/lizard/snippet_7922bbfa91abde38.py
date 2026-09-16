def on_recv(self, callback):
    if callback is None:
        self._on_recv = callback
    else:

        def wrap_recv(header, body):
            callback(body)
        self._on_recv = wrap_recv