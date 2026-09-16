def pfxmask(scope, ips, pfxlen):
    mask = ipv4.pfxlen2mask_int(pfxlen[0])
    return [ipv4.int2ip(ipv4.ip2int(ip) & mask) for ip in ips]