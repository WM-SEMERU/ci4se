def cmd_dhcp_discover(iface, timeout, verbose):
    conf.verb = False
    if iface:
        conf.iface = iface
    conf.checkIPaddr = False
    hw = get_if_raw_hwaddr(conf.iface)
    ether = Ether(dst='ff:ff:ff:ff:ff:ff')
    ip = IP(src='0.0.0.0', dst='255.255.255.255')
    udp = UDP(sport=68, dport=67)
    bootp = BOOTP(chaddr=hw)
    dhcp = DHCP(options=[('message-type', 'discover'), 'end'])
    dhcp_discover = ether / ip / udp / bootp / dhcp
    ans, unans = srp(dhcp_discover, multi=True, timeout=5)
    for _, pkt in ans:
        if verbose:
            print(pkt.show())
        else:
            print(pkt.summary())