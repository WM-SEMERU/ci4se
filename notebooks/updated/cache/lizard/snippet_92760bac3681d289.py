def get_ports(proto='tcp', direction='in'):
    proto = proto.upper()
    direction = direction.upper()
    results = {}
    _validate_direction_and_proto(direction, proto)
    directions = build_directions(direction)
    for direction in directions:
        option = '{0}_{1}'.format(proto, direction)
        results[direction] = _csf_to_list(option)
    return results