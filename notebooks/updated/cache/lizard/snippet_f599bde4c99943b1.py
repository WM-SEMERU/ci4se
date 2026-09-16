def DbGetDeviceWideList(self, argin):
    self._log.debug('In DbGetDeviceWideList()')
    argin = replace_wildcard(argin)
    return self.db.get_device_wide_list(argin)