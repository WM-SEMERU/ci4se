def _ip_int_from_string(self, ip_str):
    if not ip_str:
        raise AddressValueError('Address cannot be empty')
    octets = ip_str.split('.')
    if len(octets) != 4:
        raise AddressValueError('Expected 4 octets in %r' % ip_str)
    try:
        bvs = map(self._parse_octet, octets)
        return _compat_int_from_byte_vals(bvs, 'big')
    except ValueError as exc:
        raise AddressValueError('%s in %r' % (exc, ip_str))