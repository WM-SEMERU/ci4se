def close(self):
    if self._channel and not self._channel.handler.channel_close:
        self._channel.close()
    self._channel_ref = None