def _ip_int_from_string(cls, ip_str):
    if not ip_str:
        raise AddressValueError('Address cannot be empty')
    octets = ip_str.split('.')
    if len(octets) != 4:
        raise AddressValueError('Expected 4 octets in %r' % ip_str)
    try:
        return _compat_int_from_byte_vals(map(cls._parse_octet, octets), 'big')
    except ValueError as exc:
        raise AddressValueError('%s in %r' % (exc, ip_str))