def is_valid_ipv4(ip):
    if not _ipv4_re.match(ip):
        return False
    a, b, c, d = [int(i) for i in ip.split('.')]
    return a <= 255 and b <= 255 and c <= 255 and d <= 255