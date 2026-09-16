def stop_capture(self, slot_number, port_number):
    try:
        adapter = self._slots[slot_number]
    except IndexError:
        raise DynamipsError(
            'Slot {slot_number} does not exist on router "{name}"'.format(
            name=self._name, slot_number=slot_number))
    if not adapter.port_exists(port_number):
        raise DynamipsError(
            'Port {port_number} does not exist in adapter {adapter}'.format
            (adapter=adapter, port_number=port_number))
    nio = adapter.get_nio(port_number)
    if not nio:
        raise DynamipsError('Port {slot_number}/{port_number} is not connected'
            .format(slot_number=slot_number, port_number=port_number))
    yield from nio.unbind_filter('both')
    log.info(
        'Router "{name}" [{id}]: stopping packet capture on port {slot_number}/{port_number}'
        .format(name=self._name, id=self._id, nio_name=nio.name,
        slot_number=slot_number, port_number=port_number))