def _string_from_ip_int(self, ip_int=None):
    if not ip_int and ip_int != 0:
        ip_int = int(self._ip)
    if ip_int > self._ALL_ONES:
        raise ValueError('IPv6 address is too large')
    hex_str = '%032x' % ip_int
    hextets = []
    for x in range(0, 32, 4):
        hextets.append('%x' % int(hex_str[x:x + 4], 16))
    hextets = self._compress_hextets(hextets)
    return ':'.join(hextets)