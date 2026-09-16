def angle_to_distance(angle, units='metric'):
    distance = math.radians(angle) * BODY_RADIUS
    if units in ('km', 'metric'):
        return distance
    elif units in ('sm', 'imperial', 'US customary'):
        return distance / STATUTE_MILE
    elif units in ('nm', 'nautical'):
        return distance / NAUTICAL_MILE
    else:
        raise ValueError('Unknown units type %r' % units)