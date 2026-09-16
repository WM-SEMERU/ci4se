def get_json(self):
    port = self.get_basic_json()
    port.update({'BootProtocol': self.boot.BOOT_PROTOCOL, 'BootPriority':
        self.boot.boot_prio})
    boot_env = self.boot.get_json()
    if boot_env:
        port.update(boot_env)
    if self.use_virtual_addresses:
        addresses = {}
        if self.wwnn:
            addresses['WWNN'] = self.wwnn
        if self.wwpn:
            addresses['WWPN'] = self.wwpn
        if addresses:
            port['VirtualAddress'] = addresses
    return port