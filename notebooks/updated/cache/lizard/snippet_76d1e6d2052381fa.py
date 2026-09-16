def _changes(cur, dns_proto, dns_servers, ip_proto, ip_addrs, gateway):
    changes = {}
    cur_dns_proto = ('static' if 'Statically Configured DNS Servers' in cur
         else 'dhcp')
    if cur_dns_proto == 'static':
        if isinstance(cur['Statically Configured DNS Servers'], list):
            cur_dns_servers = cur['Statically Configured DNS Servers']
        else:
            cur_dns_servers = [cur['Statically Configured DNS Servers']]
        if set(dns_servers or ['None']) != set(cur_dns_servers):
            changes['dns_servers'] = dns_servers
    elif 'DNS servers configured through DHCP' in cur:
        cur_dns_servers = cur['DNS servers configured through DHCP']
        if dns_proto == 'static':
            if set(dns_servers or ['None']) != set(cur_dns_servers):
                changes['dns_servers'] = dns_servers
    cur_ip_proto = 'static' if cur['DHCP enabled'] == 'No' else 'dhcp'
    cur_ip_addrs = _addrdict_to_ip_addrs(cur.get('ip_addrs', []))
    cur_gateway = cur.get('Default Gateway')
    if dns_proto != cur_dns_proto:
        changes['dns_proto'] = dns_proto
    if ip_proto != cur_ip_proto:
        changes['ip_proto'] = ip_proto
    if set(ip_addrs or []) != set(cur_ip_addrs):
        if ip_proto == 'static':
            changes['ip_addrs'] = ip_addrs
    if gateway != cur_gateway:
        if ip_proto == 'static':
            changes['gateway'] = gateway
    return changes