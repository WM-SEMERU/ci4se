def query(name, rdtype, method=None, servers=None, timeout=None, walk=False,
    walk_tld=False, secure=None):
    rdtype = rdtype.upper()
    qargs = {'method': method, 'servers': servers, 'timeout': timeout,
        'walk': walk, 'walk_tld': walk_tld, 'secure': secure}
    if rdtype == 'PTR' and not name.endswith('arpa'):
        name = ptr_name(name)
    if rdtype == 'SPF':
        qres = [answer for answer in lookup(name, 'TXT', **qargs) if answer
            .startswith('v=spf')]
        if not qres:
            qres = lookup(name, rdtype, **qargs)
    else:
        qres = lookup(name, rdtype, **qargs)
    rec_map = {'A': a_rec, 'AAAA': aaaa_rec, 'CAA': caa_rec, 'MX': mx_rec,
        'SOA': soa_rec, 'SPF': spf_rec, 'SRV': srv_rec, 'SSHFP': sshfp_rec,
        'TLSA': tlsa_rec}
    if not qres or rdtype not in rec_map:
        return qres
    elif rdtype in ('A', 'AAAA', 'SSHFP', 'TLSA'):
        res = [rec_map[rdtype](res) for res in qres]
    elif rdtype in ('SOA', 'SPF'):
        res = rec_map[rdtype](qres[0])
    else:
        res = rec_map[rdtype](qres)
    return res