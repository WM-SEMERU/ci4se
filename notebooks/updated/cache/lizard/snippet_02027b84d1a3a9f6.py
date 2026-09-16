def ports(val, **kwargs):
    if not isinstance(val, list):
        try:
            val = helpers.split(val)
        except AttributeError:
            if isinstance(val, six.integer_types):
                val = [val]
            else:
                raise SaltInvocationError(
                    "'{0}' is not a valid port definition".format(val))
    new_ports = set()
    for item in val:
        if isinstance(item, six.integer_types):
            new_ports.add(item)
            continue
        try:
            item, _, proto = item.partition('/')
        except AttributeError:
            raise SaltInvocationError("'{0}' is not a valid port definition"
                .format(item))
        try:
            range_start, range_end = helpers.get_port_range(item)
        except ValueError as exc:
            raise SaltInvocationError(exc.__str__())
        new_ports.update([helpers.get_port_def(x, proto) for x in range(
            range_start, range_end + 1)])
    return list(new_ports)