def parse_host(hosts):
    hosts = EsParser._normalize_hosts(hosts)
    host = hosts[0]
    host_name = host[HostParsing.HOST]
    host_port = host[HostParsing.PORT]
    auth = None
    if HostParsing.HTTP_AUTH in host:
        http_auth = host[HostParsing.HTTP_AUTH]
        user_pass = http_auth.split(':')
        auth = user_pass[0], user_pass[1]
    full_host = '{host}:{port}'.format(host=host_name, port=host_port)
    if not host_name.startswith((HostParsing.HTTP + ':', HostParsing.HTTPS +
        ':')):
        scheme = HostParsing.HTTPS if host.get(HostParsing.USE_SSL
            ) else HostParsing.HTTP
        full_host = '{scheme}://{full_host}'.format(full_host=full_host,
            scheme=scheme)
    return full_host, auth