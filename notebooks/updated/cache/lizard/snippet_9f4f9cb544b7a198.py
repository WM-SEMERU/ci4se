def re_general(Vel, Area, PerimWetted, Nu):
    ut.check_range([Vel, '>=0', 'Velocity'], [Nu, '>0', 'Nu'])
    return 4 * radius_hydraulic_general(Area, PerimWetted).magnitude * Vel / Nu