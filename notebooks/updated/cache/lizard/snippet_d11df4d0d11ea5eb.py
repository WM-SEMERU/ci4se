def find_ip(family=AF_INET, flavour='opendns'):
    flavours = {'opendns': {AF_INET: {'@': ('resolver1.opendns.com',
        'resolver2.opendns.com'), 'qname': 'myip.opendns.com', 'rdtype':
        'A'}, AF_INET6: {'@': ('resolver1.ipv6-sandbox.opendns.com',
        'resolver2.ipv6-sandbox.opendns.com'), 'qname': 'myip.opendns.com',
        'rdtype': 'AAAA'}}}
    flavour = flavours['opendns']
    resolver = dns.resolver.Resolver()
    resolver.nameservers = [next(iter(resolve(h, family=family))) for h in
        flavour[family]['@']]
    answers = resolver.query(qname=flavour[family]['qname'], rdtype=flavour
        [family]['rdtype'])
    for rdata in answers:
        return rdata.address
    return None