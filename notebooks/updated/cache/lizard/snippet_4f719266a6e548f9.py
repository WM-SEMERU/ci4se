def _nth_str(n):
    if n % 10 == 1 and n % 100 != 11:
        return '%dst' % n
    if n % 10 == 2 and n % 100 != 12:
        return '%dnd' % n
    if n % 10 == 3 and n % 100 != 13:
        return '%drd' % n
    return '%dth' % n