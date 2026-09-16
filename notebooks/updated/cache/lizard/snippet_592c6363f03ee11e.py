def yaw(b, component, solve_for=None, **kwargs):
    hier = b.get_hierarchy()
    if not len(hier.get_value()):
        raise NotImplementedError('constraint for yaw requires hierarchy')
    component_ps = _get_system_ps(b, component)
    parentorbit = hier.get_parent_of(component)
    parentorbit_ps = _get_system_ps(b, parentorbit)
    long_an_comp = component_ps.get_parameter(qualifier='long_an')
    yaw_comp = component_ps.get_parameter(qualifier='yaw')
    long_an_orb = parentorbit_ps.get_parameter(qualifier='long_an')
    if solve_for in [None, long_an_comp]:
        lhs = long_an_comp
        rhs = long_an_orb + yaw_comp
    elif solve_for == long_an_orb:
        lhs = long_an_orb
        rhs = long_an_comp - yaw_comp
    elif solve_for == yaw_comp:
        lhs = yaw_comp
        rhs = long_an_comp - long_an_orb
    else:
        raise NotImplementedError
    return lhs, rhs, {'component': component}