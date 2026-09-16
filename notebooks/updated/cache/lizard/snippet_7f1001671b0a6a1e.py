def show(self, resolve_mac=True):
    print('%s  %s  %s  %s' % ('INDEX'.ljust(5), 'IFACE'.ljust(35), 'IP'.
        ljust(15), 'MAC'))
    for iface_name in sorted(self.data.keys()):
        dev = self.data[iface_name]
        mac = dev.mac
        if resolve_mac and iface_name != LOOPBACK_NAME:
            mac = conf.manufdb._resolve_MAC(mac)
        print('%s  %s  %s  %s' % (str(dev.win_index).ljust(5), str(dev.name
            ).ljust(35), str(dev.ip).ljust(15), mac))