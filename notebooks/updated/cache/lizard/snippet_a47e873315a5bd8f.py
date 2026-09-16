def channel(self):
    if not self._channel:
        self._channel_ref = weakref.ref(self.connection.get_channel())
    return self._channel