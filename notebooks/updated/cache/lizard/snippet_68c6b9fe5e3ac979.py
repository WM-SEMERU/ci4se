def without(self, *keys):
    items = copy(self.items)
    keys = reversed(sorted(keys))
    for key in keys:
        del items[key]
    return self.__class__(items)