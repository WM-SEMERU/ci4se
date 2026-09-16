def lookup_domain(domain, nameservers=[], rtype='A', exclude_nameservers=[],
    timeout=2):
    dns_exp = DNSQuery(domains=[domain], nameservers=nameservers, rtype=
        rtype, exclude_nameservers=exclude_nameservers, timeout=timeout)
    return dns_exp.lookup_domain(domain)