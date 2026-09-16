def findConnectedDevices(self):
    tmpTimeout = self._serial.timeout
    self._serial.timeout = 0.01
    for dev in range(128):
        device = self._getDeviceID(dev)
        if device is not None and int(device) not in self._deviceConfig:
            config = self._deviceConfig.setdefault(int(device), {})
            self._deviceCallback(device, config)
            self._log and self._log.info(
                "Found device '%s' with configuration: %s", device, config)
    self._serial.timeout = tmpTimeout