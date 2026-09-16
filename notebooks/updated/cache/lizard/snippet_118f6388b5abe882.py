def remove_from_group(self, devices):
    ids = {d.id for d in self.devices_in_group()}
    ids.difference_update(self._device_ids(devices))
    self._set_group(ids)