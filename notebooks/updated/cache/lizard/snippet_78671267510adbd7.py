def add_update_callback(self, callback, device):
    self._update_callbacks.append([callback, device])
    _LOGGER.debug('Added update callback to %s on %s', callback, device)