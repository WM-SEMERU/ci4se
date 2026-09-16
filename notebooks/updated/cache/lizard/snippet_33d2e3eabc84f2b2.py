def create_result(self, ip, host_port, container_port, meta, val, dividers):
    if host_port in ('', NotSpecified) and container_port in ('', NotSpecified
        ):
        container_port = ip
        ip = NotSpecified
        host_port = NotSpecified
    elif container_port in ('', NotSpecified):
        container_port = host_port
        host_port = ip
        ip = NotSpecified
    elif host_port in ('', NotSpecified):
        host_port = NotSpecified
    if host_port == '':
        host_port = NotSpecified
    if container_port == '':
        container_port = NotSpecified
    if host_port is not NotSpecified:
        host_port = sb.integer_spec().normalise(meta.indexed_at('host_port'
            ), host_port)
    container_port = sb.required(container_port_spec()).normalise(meta.
        indexed_at('container_port'), container_port)
    return Port(ip, host_port, container_port)