def disconnect(self, func):
    if id(self) not in _alleged_receivers:
        return
    l = _alleged_receivers[id(self)]
    try:
        l.remove(func)
    except ValueError:
        return
    if not l:
        del _alleged_receivers[id(self)]