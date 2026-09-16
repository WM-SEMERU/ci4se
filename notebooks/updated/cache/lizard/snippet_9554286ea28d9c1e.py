def one(iterable, cmp=None):
    the_one = False
    for i in iterable:
        if cmp(i) if cmp else i:
            if the_one:
                return False
            the_one = i
    return the_one