def broadcast(self, destination, message, **kwargs):
    message = self._mangle_for_sending(message)
    self._broadcast(destination, message, **kwargs)