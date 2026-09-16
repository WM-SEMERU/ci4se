def DbGetExportdDeviceListForClass(self, argin):
    self._log.debug('In DbGetExportdDeviceListForClass()')
    argin = replace_wildcard(argin)
    return self.db.get_exported_device_list_for_class(argin)