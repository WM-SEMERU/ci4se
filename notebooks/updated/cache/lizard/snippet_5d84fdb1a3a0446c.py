def human_time(seconds):
    units = [('y', 60 * 60 * 24 * 7 * 52), ('w', 60 * 60 * 24 * 7), ('d', 
        60 * 60 * 24), ('h', 60 * 60), ('m', 60), ('s', 1)]
    seconds = int(seconds)
    if seconds < 60:
        return '   {0:2d}s'.format(seconds)
    for i in range(len(units) - 1):
        unit1, limit1 = units[i]
        unit2, limit2 = units[i + 1]
        if seconds >= limit1:
            return '{0:2d}{1}{2:2d}{3}'.format(seconds // limit1, unit1, 
                seconds % limit1 // limit2, unit2)
    return '  ~inf'