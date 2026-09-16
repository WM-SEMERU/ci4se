def parse_host_port(host_port):
    host, port = None, None
    _s_ = host_port[:]
    if _s_[0] == '[':
        if ']' in host_port:
            host, _s_ = _s_.lstrip('[').rsplit(']', 1)
            host = ipaddress.IPv6Address(host).compressed
            if _s_[0] == ':':
                port = int(_s_.lstrip(':'))
            elif len(_s_) > 1:
                raise ValueError('found ambiguous "{}" port in "{}"'.format
                    (_s_, host_port))
    elif _s_.count(':') == 1:
        host, _hostport_separator_, port = _s_.partition(':')
        try:
            port = int(port)
        except ValueError as _e_:
            log.error('host_port "%s" port value "%s" is not an integer.',
                host_port, port)
            raise _e_
    else:
        host = _s_
    try:
        if not isinstance(host, ipaddress._BaseAddress):
            host_ip = ipaddress.ip_address(host).compressed
            host = host_ip
    except ValueError:
        log.debug('"%s" Not an IP address? Assuming it is a hostname.', host)
        if host != sanitize_host(host):
            log.error('bad hostname: "%s"', host)
            raise ValueError('bad hostname: "{}"'.format(host))
    return host, port