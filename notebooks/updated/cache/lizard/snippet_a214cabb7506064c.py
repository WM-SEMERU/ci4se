def stream_messages(self):
    if self._stream_messages is None:
        self._stream_messages = StreamMessageList(self._version,
            service_sid=self._solution['service_sid'], stream_sid=self.
            _solution['sid'])
    return self._stream_messages