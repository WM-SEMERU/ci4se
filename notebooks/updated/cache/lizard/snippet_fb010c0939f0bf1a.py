def in6_isincluded(addr, prefix, plen):
    temp = inet_pton(socket.AF_INET6, addr)
    pref = in6_cidr2mask(plen)
    zero = inet_pton(socket.AF_INET6, prefix)
    return zero == in6_and(temp, pref)