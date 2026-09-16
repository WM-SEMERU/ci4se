def get_value_unit(value, unit, prefix):
    prefixes = '', 'K', 'M', 'G', 'T'
    if len(unit):
        if unit[:1] in prefixes:
            valprefix = unit[0]
            unit = unit[1:]
        else:
            valprefix = ''
    else:
        valprefix = ''
    while valprefix != prefix:
        uidx = prefixes.index(valprefix)
        if uidx > prefixes.index(prefix):
            value *= 1024
            valprefix = prefixes[uidx - 1]
        else:
            if value < 10240:
                return value, '{0}{1}'.format(valprefix, unit)
            value = int(round(value / 1024.0))
            valprefix = prefixes[uidx + 1]
    return value, '{0}{1}'.format(valprefix, unit)