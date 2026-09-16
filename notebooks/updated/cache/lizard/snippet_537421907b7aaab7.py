def delete(self, interface, vrid):
    vrrp_str = 'no vrrp %d' % vrid
    return self.configure_interface(interface, vrrp_str)