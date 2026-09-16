def in6_getha(prefix):
    r = in6_and(inet_pton(socket.AF_INET6, prefix), in6_cidr2mask(64))
    r = in6_or(r, inet_pton(socket.AF_INET6, '::fdff:ffff:ffff:fffe'))
    return inet_ntop(socket.AF_INET6, r)