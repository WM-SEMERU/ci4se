def reset(self):
    self._text = None
    self._markdown = False
    self._channel = Incoming.DEFAULT_CHANNEL
    self._attachments = []
    return self