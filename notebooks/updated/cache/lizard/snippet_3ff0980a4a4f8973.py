def slot_remove_nio_binding(self, slot_number, port_number):
    try:
        adapter = self._slots[slot_number]
    except IndexError:
        raise DynamipsError(
            'Slot {slot_number} does not exist on router "{name}"'.format(
            name=self._name, slot_number=slot_number))
    if adapter is None:
        raise DynamipsError('Adapter is missing in slot {slot_number}'.
            format(slot_number=slot_number))
    if not adapter.port_exists(port_number):
        raise DynamipsError(
            'Port {port_number} does not exist in adapter {adapter}'.format
            (adapter=adapter, port_number=port_number))
    yield from self.slot_disable_nio(slot_number, port_number)
    yield from self._hypervisor.send(
        'vm slot_remove_nio_binding "{name}" {slot_number} {port_number}'.
        format(name=self._name, slot_number=slot_number, port_number=
        port_number))
    nio = adapter.get_nio(port_number)
    if nio is None:
        return
    yield from nio.close()
    adapter.remove_nio(port_number)
    log.info(
        'Router "{name}" [{id}]: NIO {nio_name} removed from port {slot_number}/{port_number}'
        .format(name=self._name, id=self._id, nio_name=nio.name,
        slot_number=slot_number, port_number=port_number))
    return nio