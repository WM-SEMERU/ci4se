def popitem(self):
    try:
        key = self.__choice(list(self))
    except IndexError:
        raise KeyError('%s is empty' % self.__class__.__name__)
    else:
        return key, self.pop(key)