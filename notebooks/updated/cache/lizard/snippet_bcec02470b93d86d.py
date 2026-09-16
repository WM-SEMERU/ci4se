def dns():
    if salt.utils.platform.is_windows() or 'proxyminion' in __opts__:
        return {}
    resolv = salt.utils.dns.parse_resolv()
    for key in ('nameservers', 'ip4_nameservers', 'ip6_nameservers', 'sortlist'
        ):
        if key in resolv:
            resolv[key] = [six.text_type(i) for i in resolv[key]]
    return {'dns': resolv} if resolv else {}