def set_mac_addr_adv_interval(self, name, vrid, value=None, disable=False,
    default=False, run=True):
    if not default and not disable:
        if not int(value) or int(value) < 1 or int(value) > 3600:
            raise ValueError(
                "vrrp property 'mac_addr_adv_interval' must be in the range 1-3600"
                )
    cmd = self.command_builder('vrrp %d mac-address advertisement-interval' %
        vrid, value=value, default=default, disable=disable)
    if run:
        result = self.configure_interface(name, cmd)
        if result is False:
            return self.error
        return result
    return cmd