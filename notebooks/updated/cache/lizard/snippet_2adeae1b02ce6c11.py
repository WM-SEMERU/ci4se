def parameter_value(self, parameter, read_cached=True):
    if parameter == MI_BATTERY:
        return self.battery_level()
    with self.lock:
        if read_cached is False or self._last_read is None or datetime.now(
            ) - self._cache_timeout > self._last_read:
            self.fill_cache()
        else:
            _LOGGER.debug('Using cache (%s < %s)', datetime.now() - self.
                _last_read, self._cache_timeout)
    if self.cache_available() and len(self._cache) == 16:
        return self._parse_data()[parameter]
    else:
        raise BluetoothBackendException(
            'Could not read data from Mi Flora sensor %s' % self._mac)