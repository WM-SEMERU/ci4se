def scan(self):
    self._logger.info("iface '%s' scans", self.name())
    self._wifi_ctrl.scan(self._raw_obj)