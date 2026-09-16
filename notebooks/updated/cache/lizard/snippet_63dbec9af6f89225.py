def get_whois_tags(ip_address):
    whois = IPWhois(ip_address).lookup_whois()
    nets = whois.get('nets', None)
    if not nets:
        return []
    cities = [net['city'] for net in nets if net.get('city', None)]
    address_list = []
    for net in nets:
        address = net.get('address', None)
        if not address:
            continue
        if 'description' in net and net['description']:
            address = address.replace(net['description'], '').strip()
        if '\n' in address:
            address = ', '.join(address.splitlines())
        address_list.append(address)
    return [SourceString(val, source='Whois') for val in set(cities +
        address_list)]