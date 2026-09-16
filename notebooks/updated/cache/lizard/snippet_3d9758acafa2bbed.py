def _reachable_subsystems(network, indices, state):
    validate.is_network(network)
    for subset in utils.powerset(indices, nonempty=True, reverse=True):
        try:
            yield Subsystem(network, state, subset)
        except exceptions.StateUnreachableError:
            pass