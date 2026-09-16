def calc_avgstrlen_pathstextnodes(pars_tnodes, dbg=False):
    ttl = 0
    for _, tnodes in pars_tnodes:
        ttl += tnodes[3]
    crd = len(pars_tnodes)
    avg = ttl / crd
    if dbg is True:
        print(avg)
    return avg, ttl, crd