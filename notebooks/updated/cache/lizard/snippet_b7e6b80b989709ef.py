def adapters(self, adapters):
    if adapters > 10:
        raise VMwareError(
            'Number of adapters above the maximum supported of 10')
    self._ethernet_adapters.clear()
    for adapter_number in range(0, adapters):
        self._ethernet_adapters[adapter_number] = EthernetAdapter()
    self._adapters = len(self._ethernet_adapters)
    log.info(
        "VMware VM '{name}' [{id}] has changed the number of Ethernet adapters to {adapters}"
        .format(name=self.name, id=self.id, adapters=adapters))