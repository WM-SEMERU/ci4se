def collapse_address_list(addresses):
    i = 0
    addrs = []
    ips = []
    nets = []
    for ip in addresses:
        if isinstance(ip, _BaseIP):
            if ips and ips[-1]._version != ip._version:
                raise TypeError('%s and %s are not of the same version' % (
                    str(ip), str(ips[-1])))
            ips.append(ip)
        elif ip._prefixlen == ip._max_prefixlen:
            if ips and ips[-1]._version != ip._version:
                raise TypeError('%s and %s are not of the same version' % (
                    str(ip), str(ips[-1])))
            ips.append(ip.ip)
        else:
            if nets and nets[-1]._version != ip._version:
                raise TypeError('%s and %s are not of the same version' % (
                    str(ip), str(nets[-1])))
            nets.append(ip)
    ips = sorted(set(ips))
    nets = sorted(set(nets))
    while i < len(ips):
        first, last = _find_address_range(ips[i:])
        i = ips.index(last) + 1
        addrs.extend(summarize_address_range(first, last))
    return _collapse_address_list_recursive(sorted(addrs + nets, key=
        _BaseNet._get_networks_key))