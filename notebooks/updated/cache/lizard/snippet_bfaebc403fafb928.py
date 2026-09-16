def iterable(target):
    if any(i in ('next', '__next__', '__iter__') for i in dir(target)):
        return True
    else:
        try:
            iter(target)
            return True
        except:
            return False