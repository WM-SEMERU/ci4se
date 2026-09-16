def DbPutDeviceAttributeProperty2(self, argin):
    self._log.debug('In DbPutDeviceAttributeProperty2()')
    device_name = argin[0]
    nb_attributes = int(argin[1])
    self.db.put_device_attribute_property2(device_name, nb_attributes,
        argin[2:])