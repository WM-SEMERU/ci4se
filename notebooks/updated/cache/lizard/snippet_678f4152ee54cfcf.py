def _fullname(o):
    return o.__module__ + '.' + o.__name__ if o.__module__ else o.__name__