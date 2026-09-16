def boost_error_level(version, error, segments, eci, is_sa=False):
    if error not in (consts.ERROR_LEVEL_H, None) and len(segments) == 1:
        levels = [consts.ERROR_LEVEL_L, consts.ERROR_LEVEL_M, consts.
            ERROR_LEVEL_Q, consts.ERROR_LEVEL_H]
        if version < 1:
            levels.pop()
            if version < consts.VERSION_M4:
                levels.pop()
        data_length = segments.bit_length_with_overhead(version, eci, is_sa
            =is_sa)
        for level in levels[levels.index(error) + 1:]:
            try:
                found = consts.SYMBOL_CAPACITY[version][level] >= data_length
            except KeyError:
                break
            if found:
                error = level
    return error