def position(msg0, msg1, t0, t1, lat_ref=None, lon_ref=None):
    tc0 = typecode(msg0)
    tc1 = typecode(msg1)
    if 5 <= tc0 <= 8 and 5 <= tc1 <= 8:
        if not lat_ref or not lon_ref:
            raise RuntimeError(
                'Surface position encountered, a reference                                position lat/lon required. Location of                                receiver can be used.'
                )
        else:
            return surface_position(msg0, msg1, t0, t1, lat_ref, lon_ref)
    elif 9 <= tc0 <= 18 and 9 <= tc1 <= 18:
        return airborne_position(msg0, msg1, t0, t1)
    elif 20 <= tc0 <= 22 and 20 <= tc1 <= 22:
        return airborne_position(msg0, msg1, t0, t1)
    else:
        raise RuntimeError('incorrect or inconsistant message types')