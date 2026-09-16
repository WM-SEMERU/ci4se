def fill_cache(self):
    _LOGGER.debug('Filling cache with new sensor data.')
    try:
        firmware_version = self.firmware_version()
    except BluetoothBackendException:
        self._last_read = datetime.now() - self._cache_timeout + timedelta(
            seconds=300)
        raise
    with self._bt_interface.connect(self._mac) as connection:
        if firmware_version >= '2.6.6':
            try:
                connection.write_handle(_HANDLE_WRITE_MODE_CHANGE,
                    _DATA_MODE_CHANGE)
            except BluetoothBackendException:
                self._last_read = datetime.now(
                    ) - self._cache_timeout + timedelta(seconds=300)
                return
        self._cache = connection.read_handle(_HANDLE_READ_SENSOR_DATA)
        _LOGGER.debug('Received result for handle %s: %s',
            _HANDLE_READ_SENSOR_DATA, self._format_bytes(self._cache))
        self._check_data()
        if self.cache_available():
            self._last_read = datetime.now()
        else:
            self._last_read = datetime.now() - self._cache_timeout + timedelta(
                seconds=300)