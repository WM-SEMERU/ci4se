def popitem(self):
    try:
        (key, _), = self.__counter.most_common(1)
    except ValueError:
        raise KeyError('%s is empty' % self.__class__.__name__)
    else:
        return key, self.pop(key)