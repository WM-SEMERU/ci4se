def set_disk0(self, disk0):
    yield from self._hypervisor.send('vm set_disk0 "{name}" {disk0}'.format
        (name=self._name, disk0=disk0))
    log.info(
        'Router "{name}" [{id}]: disk0 updated from {old_disk0}MB to {new_disk0}MB'
        .format(name=self._name, id=self._id, old_disk0=self._disk0,
        new_disk0=disk0))
    self._disk0 = disk0