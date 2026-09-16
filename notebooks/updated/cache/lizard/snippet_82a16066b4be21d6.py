def _process_removed_port(self, device):
    LOG.debug('Trying to remove the port %r', device)
    self._update_port_status_cache(device, device_bound=False)
    self._port_unbound(device, vnic_deleted=True)
    LOG.debug('The port was successfully removed.')
    self._removed_ports.discard(device)