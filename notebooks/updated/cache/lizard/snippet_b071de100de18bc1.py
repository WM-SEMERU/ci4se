def _make_netmask(cls, arg):
    if arg not in cls._netmask_cache:
        if isinstance(arg, _compat_int_types):
            prefixlen = arg
        else:
            prefixlen = cls._prefix_from_prefix_string(arg)
        netmask = IPv6Address(cls._ip_int_from_prefix(prefixlen))
        cls._netmask_cache[arg] = netmask, prefixlen
    return cls._netmask_cache[arg]