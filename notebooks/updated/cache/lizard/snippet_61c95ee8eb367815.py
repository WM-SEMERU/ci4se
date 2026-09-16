def rand_hexstr(length, lower=True):
    if lower:
        return rand_str(length, allowed=CHARSET_HEXSTR_LOWER)
    else:
        return rand_str(length, allowed=CHARSET_HEXSTR_UPPER)