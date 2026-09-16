def close(self):
    if self._channel and self._channel.is_open:
        self._channel.close()
    self._channel_ref = None