def devices(self):
    eax = self.attributes.get('devices')
    if eax is None:
        eax = self._all_devices
    if not isinstance(eax, list):
        eax = [eax]
    return [str(dev) for dev in eax]