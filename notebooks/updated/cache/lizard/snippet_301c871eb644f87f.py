def adapter_remove_nio_binding(self, adapter_number):
    try:
        adapter = self._ethernet_adapters[adapter_number]
    except IndexError:
        raise DockerError(
            "Adapter {adapter_number} doesn't exist on Docker VM '{name}'".
            format(name=self.name, adapter_number=adapter_number))
    if self.ubridge:
        nio = adapter.get_nio(0)
        bridge_name = 'bridge{}'.format(adapter_number)
        yield from self._ubridge_send('bridge stop {}'.format(bridge_name))
        yield from self._ubridge_send(
            'bridge remove_nio_udp bridge{adapter} {lport} {rhost} {rport}'
            .format(adapter=adapter_number, lport=nio.lport, rhost=nio.
            rhost, rport=nio.rport))
    adapter.remove_nio(0)
    log.info(
        "Docker VM '{name}' [{id}]: {nio} removed from adapter {adapter_number}"
        .format(name=self.name, id=self.id, nio=adapter.host_ifc,
        adapter_number=adapter_number))