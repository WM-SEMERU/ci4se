def _do_new_devices_callback(self, msg):
    for callback in self._new_devices_callbacks:
        _LOGGER.debug('Devices callback %s', callback)
        self._event_loop.call_soon(callback, msg)