def in6_ptoc(addr):
    try:
        d = struct.unpack('!IIII', inet_pton(socket.AF_INET6, addr))
    except Exception:
        return None
    res = 0
    m = [2 ** 96, 2 ** 64, 2 ** 32, 1]
    for i in range(4):
        res += d[i] * m[i]
    rem = res
    res = []
    while rem:
        res.append(_rfc1924map[rem % 85])
        rem = rem // 85
    res.reverse()
    return ''.join(res)