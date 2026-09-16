def print_all_aldb(self):
    addr = self.plm.address.id
    _LOGGING.info('ALDB for PLM device %s', addr)
    self.print_device_aldb(addr)
    if self.plm.devices:
        for addr in self.plm.devices:
            _LOGGING.info('ALDB for device %s', addr)
            self.print_device_aldb(addr)
    else:
        _LOGGING.info('No devices found')
        if not self.plm.transport:
            _LOGGING.info('IM connection has not been made.')
            _LOGGING.info('Use `connect [device]` to open the connection')