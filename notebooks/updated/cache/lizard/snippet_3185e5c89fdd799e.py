def from_rdata_list(name, ttl, rdatas):
    if isinstance(name, (str, unicode)):
        name = dns.name.from_text(name, None)
    if len(rdatas) == 0:
        raise ValueError('rdata list must not be empty')
    r = None
    for rd in rdatas:
        if r is None:
            r = RRset(name, rd.rdclass, rd.rdtype)
            r.update_ttl(ttl)
            first_time = False
        r.add(rd)
    return r