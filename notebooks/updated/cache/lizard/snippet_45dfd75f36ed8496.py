def traceroute(destination, source=None, ttl=None, timeout=None, vrf=None,
    **kwargs):
    return salt.utils.napalm.call(napalm_device, 'traceroute', **{
        'destination': destination, 'source': source, 'ttl': ttl, 'timeout':
        timeout, 'vrf': vrf})