def fuzzy_int(str_):
    try:
        ret = int(str_)
        return ret
    except Exception:
        if re.match('\\d*,\\d*,?\\d*', str_):
            return tuple(map(int, str_.split(',')))
        if re.match('\\d*:\\d*:?\\d*', str_):
            return tuple(range(*map(int, str_.split(':'))))
        raise