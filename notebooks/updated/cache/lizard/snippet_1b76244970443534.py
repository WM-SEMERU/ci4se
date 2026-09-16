def _AddForwardedIps(self, forwarded_ips, interface):
    for address in forwarded_ips:
        self.ip_forwarding_utils.AddForwardedIp(address, interface)