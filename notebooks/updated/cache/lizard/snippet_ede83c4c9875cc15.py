def parse_to_gvid(v):
    from geoid.civick import GVid
    from geoid.acs import AcsGeoid
    m1 = ''
    try:
        return GVid.parse(v)
    except ValueError as e:
        m1 = str(e)
    try:
        return AcsGeoid.parse(v).convert(GVid)
    except ValueError as e:
        raise ValueError('Failed to parse to either ACS or GVid: {}; {}'.
            format(m1, str(e)))