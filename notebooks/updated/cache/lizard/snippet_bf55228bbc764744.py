def toString(value, mode):
    string = angle.toString(value)
    sign = string[0]
    separator = CHAR[mode][sign]
    string = string.replace(':', separator, 1)
    return string[1:]