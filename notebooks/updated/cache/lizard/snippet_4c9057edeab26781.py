def update(zone, name, ttl, rdtype, data, nameserver='127.0.0.1', timeout=5,
    replace=False, port=53, **kwargs):
    name = six.text_type(name)
    if name[-1:] == '.':
        fqdn = name
    else:
        fqdn = '{0}.{1}'.format(name, zone)
    request = dns.message.make_query(fqdn, rdtype)
    answer = dns.query.udp(request, nameserver, timeout, port)
    rdtype = dns.rdatatype.from_text(rdtype)
    rdata = dns.rdata.from_text(dns.rdataclass.IN, rdtype, data)
    keyring = _get_keyring(_config('keyfile', **kwargs))
    keyname = _config('keyname', **kwargs)
    keyalgorithm = _config('keyalgorithm', **kwargs
        ) or 'HMAC-MD5.SIG-ALG.REG.INT'
    is_exist = False
    for rrset in answer.answer:
        if rdata in rrset.items:
            if ttl == rrset.ttl:
                if len(answer.answer) >= 1 or len(rrset.items) >= 1:
                    is_exist = True
                    break
    dns_update = dns.update.Update(zone, keyring=keyring, keyname=keyname,
        keyalgorithm=keyalgorithm)
    if replace:
        dns_update.replace(name, ttl, rdata)
    elif not is_exist:
        dns_update.add(name, ttl, rdata)
    else:
        return None
    answer = dns.query.udp(dns_update, nameserver, timeout, port)
    if answer.rcode() > 0:
        return False
    return True