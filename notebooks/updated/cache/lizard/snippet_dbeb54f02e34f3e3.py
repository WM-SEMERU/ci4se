def padStr(s, field=None):
    if field is None:
        return s
    elif len(s) >= field:
        return s
    else:
        return ' ' * (field - len(s)) + s