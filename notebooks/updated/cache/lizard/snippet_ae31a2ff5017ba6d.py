def connect(self):
    if self._port:
        self._driver = MagDeckDriver()
        self._driver.connect(self._port)
        self._device_info = self._driver.get_device_info()
    else:
        raise MissingDevicePortError('MagDeck couldnt connect to port {}'.
            format(self._port))