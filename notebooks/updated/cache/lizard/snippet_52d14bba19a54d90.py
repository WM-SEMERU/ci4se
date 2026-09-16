def escape_vals(vals, escape_numerics=True):
    ints, floats = '%.1f', '%.10f'
    escaped = []
    for v in vals:
        if isinstance(v, np.timedelta64):
            v = "'" + str(v) + "'"
        elif isinstance(v, np.datetime64):
            v = "'" + str(v.astype('datetime64[ns]')) + "'"
        elif not isnumeric(v):
            v = "'" + unicode(bytes_to_unicode(v)) + "'"
        else:
            if v % 1 == 0:
                v = ints % v
            else:
                v = (floats % v)[:-1]
            if escape_numerics:
                v = "'" + v + "'"
        escaped.append(v)
    return escaped