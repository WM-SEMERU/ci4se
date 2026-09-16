def allow_ports(ports, proto='tcp', direction='in'):
    results = []
    ports = set(ports)
    ports = list(ports)
    proto = proto.upper()
    direction = direction.upper()
    _validate_direction_and_proto(direction, proto)
    ports_csv = ','.join(six.moves.map(six.text_type, ports))
    directions = build_directions(direction)
    for direction in directions:
        result = __salt__['file.replace']('/etc/csf/csf.conf', pattern=
            '^{0}_{1}(\\ +)?\\=(\\ +)?".*"$'.format(proto, direction), repl
            ='{0}_{1} = "{2}"'.format(proto, direction, ports_csv))
        results.append(result)
    return results