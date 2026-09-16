def registerDisplay(func):
    setup()
    ref = weakref.ref(func)
    if ref not in _displayhooks:
        _displayhooks.append(ref)