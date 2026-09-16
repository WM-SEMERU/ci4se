def connect(self, mac: str):
    import pygatt
    address_type = pygatt.BLEAddressType.public
    if self._address_type == 'random':
        address_type = pygatt.BLEAddressType.random
    self._device = self._adapter.connect(mac, address_type=address_type)