def cast_value(val, totype):
    t = type(val)
    if issubclass(t, totype):
        return val
    if issubclass(totype, bytes):
        return bytes(val)
    if issubclass(totype, str):
        return str(val)
    if issubclass(totype, bool):
        if issubclass(t, str):
            _v = val.lower()
            if _v in ('true', 'yes', 'y'):
                return True
            if _v in ('false', 'no', 'n'):
                return False
            raise TypeError('Not able to cast value: ' + str(val) +
                ' with ' + str(t) + ' to ' + str(totype))
    if issubclass(totype, (int, float)) and issubclass(t, (bytes, str, int,
        float)):
        if val:
            return totype(float(val))
        else:
            return totype(0)
    raise TypeError('Not able to cast value:' + str(val) + ' with ' + str(t
        ) + ' to ' + str(totype))