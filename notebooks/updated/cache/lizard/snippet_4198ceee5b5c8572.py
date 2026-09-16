def _parse_protocol_port(name, protocol, port):
    protocol_port_pattern = '^(tcp|udp)\\/(([\\d]+)\\-?[\\d]+)$'
    name_parts = re.match(protocol_port_pattern, name)
    if not name_parts:
        name_parts = re.match(protocol_port_pattern, '{0}/{1}'.format(
            protocol, port))
    if not name_parts:
        raise SaltInvocationError(
            'Invalid name "{0}" format and protocol and port not provided or invalid: "{1}" "{2}".'
            .format(name, protocol, port))
    return name_parts.group(1), name_parts.group(2)