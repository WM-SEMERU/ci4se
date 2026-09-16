def is_dn(s):
    if s == '':
        return True
    rm = DN_REGEX.match(s)
    return rm is not None and rm.group(0) == s