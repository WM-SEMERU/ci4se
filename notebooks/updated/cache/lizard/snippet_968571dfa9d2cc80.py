def _validate_states(states, topology):
    states = states or []
    if isinstance(states, dict):
        for x in states:
            assert x in topology.node
    else:
        assert len(states) <= len(topology)
    return states