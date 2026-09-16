def getauthority(self, default=None, encoding='utf-8', errors='strict'):
    if default is None:
        default = None, None, None
    elif not isinstance(default, collections.Iterable):
        raise TypeError('Invalid default type')
    elif len(default) != 3:
        raise ValueError('Invalid default length')
    return self.getuserinfo(default[0], encoding, errors), self.gethost(default
        [1], errors), self.getport(default[2])