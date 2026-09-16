def in6_cidr2mask(m):
    if m > 128 or m < 0:
        raise Kamene_Exception(
            'value provided to in6_cidr2mask outside [0, 128] domain (%d)' % m)
    t = []
    for i in range(0, 4):
        t.append(max(0, 2 ** 32 - 2 ** (32 - min(32, m))))
        m -= 32
    return b''.join([struct.pack('!I', i) for i in t])