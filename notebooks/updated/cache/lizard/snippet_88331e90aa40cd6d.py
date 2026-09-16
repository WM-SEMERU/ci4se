def run(self, request_cb, notification_cb):
    self._request_cb = request_cb
    self._notification_cb = notification_cb
    self._msgpack_stream.run(self._on_message)
    self._request_cb = None
    self._notification_cb = None