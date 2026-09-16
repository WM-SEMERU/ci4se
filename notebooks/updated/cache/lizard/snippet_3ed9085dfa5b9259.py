def _init_dbus(self):
    _bus = SessionBus()
    if self.device_id is None:
        self.device_id = self._get_device_id(_bus)
        if self.device_id is None:
            return False
    try:
        self._dev = _bus.get(SERVICE_BUS, DEVICE_PATH + '/%s' % self.device_id)
    except Exception:
        return False
    return True