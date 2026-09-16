def active_network_addresses(hypervisor):
    active = []
    for network in hypervisor.listNetworks():
        try:
            xml = hypervisor.networkLookupByName(network).XMLDesc(0)
        except libvirt.libvirtError:
            continue
        else:
            ip_element = etree.fromstring(xml).find('.//ip')
            address = ip_element.get('address')
            netmask = ip_element.get('netmask')
            active.append(ipaddress.IPv4Network('/'.join((address, netmask)
                ), strict=False))
    return active