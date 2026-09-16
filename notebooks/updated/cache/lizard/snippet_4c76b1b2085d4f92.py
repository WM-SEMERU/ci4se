def StartsWith(this, that):
    this_iter = iter(this)
    that_iter = iter(that)
    while True:
        try:
            this_value = next(that_iter)
        except StopIteration:
            return True
        try:
            that_value = next(this_iter)
        except StopIteration:
            return False
        if this_value != that_value:
            return False