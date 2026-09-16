def rsplit(_str, seps):
    for idx, ch in enumerate(reversed(_str)):
        if ch in seps:
            return _str[0:-idx - 1], _str[-idx:]