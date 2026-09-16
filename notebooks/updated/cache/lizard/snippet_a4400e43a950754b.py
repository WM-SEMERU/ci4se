def check_nodes_count(baremetal_client, stack, parameters, defaults):
    count = 0
    if stack:
        for param in defaults:
            try:
                current = int(stack.parameters[param])
            except KeyError:
                raise ValueError(
                    "Parameter '%s' was not found in existing stack" % param)
            count += parameters.get(param, current)
    else:
        for param, default in defaults.items():
            count += parameters.get(param, default)
    available = len(baremetal_client.node.list(associated=False,
        maintenance=False))
    if count > available:
        raise exceptions.DeploymentError(
            'Not enough nodes - available: {0}, requested: {1}'.format(
            available, count))
    else:
        return True