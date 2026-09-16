def ping(destination, source=None, ttl=None, timeout=None, size=None, count
    =None, vrf=None, **kwargs):
    return salt.utils.napalm.call(napalm_device, 'ping', **{'destination':
        destination, 'source': source, 'ttl': ttl, 'timeout': timeout,
        'size': size, 'count': count, 'vrf': vrf})