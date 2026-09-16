def is_private(ip):
    if matches_prefix(ip, '10.0.0.0/8'):
        return True
    if matches_prefix(ip, '172.16.0.0/12'):
        return True
    if matches_prefix(ip, '192.168.0.0/16'):
        return True
    return False