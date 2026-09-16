def _split_optional_netmask(address):
    addr = _compat_str(address).split('/')
    if len(addr) > 2:
        raise AddressValueError("Only one '/' permitted in %r" % address)
    return addr