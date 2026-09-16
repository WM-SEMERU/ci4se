def hex2ip(hex_ip, invert=False):
    if len(hex_ip) == 32:
        ip = []
        for i in range(0, 32, 8):
            ip_part = hex_ip[i:i + 8]
            ip_part = [ip_part[x:x + 2] for x in range(0, 8, 2)]
            if invert:
                ip.append('{0[3]}{0[2]}:{0[1]}{0[0]}'.format(ip_part))
            else:
                ip.append('{0[0]}{0[1]}:{0[2]}{0[3]}'.format(ip_part))
        try:
            address = ipaddress.IPv6Address(':'.join(ip))
            if address.ipv4_mapped:
                return str(address.ipv4_mapped)
            else:
                return address.compressed
        except ipaddress.AddressValueError as ex:
            log.error('hex2ip - ipv6 address error: %s', ex)
            return hex_ip
    try:
        hip = int(hex_ip, 16)
    except ValueError:
        return hex_ip
    if invert:
        return '{3}.{2}.{1}.{0}'.format(hip >> 24 & 255, hip >> 16 & 255, 
            hip >> 8 & 255, hip & 255)
    return '{0}.{1}.{2}.{3}'.format(hip >> 24 & 255, hip >> 16 & 255, hip >>
        8 & 255, hip & 255)