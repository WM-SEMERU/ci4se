def remove(self, elem):
    self._values.remove(elem)
    self._message_listener.Modified()