def update(self):
    with self._lock:
        devices = self._request_devices(MINUT_DEVICES_URL, 'devices')
        if devices:
            self._state = {device['device_id']: device for device in devices}
            _LOGGER.debug('Found devices: %s', list(self._state.keys()))
        homes = self._request_devices(MINUT_HOMES_URL, 'homes')
        if homes:
            self._homes = homes
        return self.devices