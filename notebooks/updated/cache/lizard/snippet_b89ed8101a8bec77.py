def subsystem(s):
    node_states(s.state)
    cut(s.cut, s.cut_indices)
    if config.VALIDATE_SUBSYSTEM_STATES:
        state_reachable(s)
    return True