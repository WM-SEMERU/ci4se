def getter(name, key=None):
    if not key:
        key = lambda x: x

    def wrapper(self):
        return key(getattr(self, name))
    wrapper.__name__ = wrapper.__qualname__ = name
    return property(wrapper)