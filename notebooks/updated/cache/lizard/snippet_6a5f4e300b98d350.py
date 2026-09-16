def expected_related_units(reltype=None):
    if not has_juju_version('2.4.4'):
        raise NotImplementedError('goal-state relation unit count')
    reltype = reltype or relation_type()
    _goal_state = goal_state()
    return (key for key in _goal_state['relations'][reltype] if '/' in key)