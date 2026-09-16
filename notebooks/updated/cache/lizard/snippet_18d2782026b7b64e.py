def get_device_types_for_storage_bus(self, bus):
    if not isinstance(bus, StorageBus):
        raise TypeError('bus can only be an instance of type StorageBus')
    device_types = self._call('getDeviceTypesForStorageBus', in_p=[bus])
    device_types = [DeviceType(a) for a in device_types]
    return device_types