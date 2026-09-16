def oem_init(self):
    if self._oemknown:
        return
    self._oem, self._oemknown = get_oem_handler(self._get_device_id(), self)