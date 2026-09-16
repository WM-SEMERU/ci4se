def compare_locales(a, b):
    if a is None or b is None:
        if a == b:
            return 2
        else:
            return 0
    a = split_locale(a)
    b = split_locale(b)
    if a == b:
        return 2
    elif a[0] == b[0]:
        return 1
    else:
        return 0