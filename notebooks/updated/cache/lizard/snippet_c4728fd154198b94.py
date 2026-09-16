def time_from_hhmmssmmm(string, decimal_separator='.'):
    if decimal_separator == ',':
        pattern = HHMMSS_MMM_PATTERN_COMMA
    else:
        pattern = HHMMSS_MMM_PATTERN
    v_length = TimeValue('0.000')
    try:
        match = pattern.search(string)
        if match is not None:
            v_h = int(match.group(1))
            v_m = int(match.group(2))
            v_s = int(match.group(3))
            v_f = TimeValue('0.' + match.group(4))
            v_length = v_h * 3600 + v_m * 60 + v_s + v_f
    except:
        pass
    return v_length