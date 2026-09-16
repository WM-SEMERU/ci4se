def DbDeleteAllDeviceAttributeProperty(self, argin):
    self._log.debug('In DbDeleteAllDeviceAttributeProperty()')
    if len(argin) < 2:
        self.warn_stream(
            'DataBase::DbDeleteAllDeviceAttributeProperty(): insufficient number of arguments '
            )
        th_exc(DB_IncorrectArguments,
            'insufficient number of arguments to delete all device attribute(s) property'
            , 'DataBase::DbDeleteAllDeviceAttributeProperty()')
    dev_name = argin[0]
    ret, d_name, dfm = check_device_name(dev_name)
    if not ret:
        th_exc(DB_IncorrectDeviceName, 'device name (' + argin +
            ') syntax error (should be [tango:][//instance/]domain/family/member)'
            , 'DataBase::DbDeleteAllDeviceAttributeProperty()')
    self.db.delete_all_device_attribute_property(dev_name, argin[1:])