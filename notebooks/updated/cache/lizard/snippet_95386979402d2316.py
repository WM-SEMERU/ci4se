def get(self, name, strict=True):
    if not isinstance(name, str) or name.startswith('_'):
        raise AttributeError(self.__class__.__name__, name)
    elif strict and name not in self._possible_attributes:
        raise AttributeError('%s is not a valid attribute of %r.' % (name,
            self))
    elif name in self._attributes:
        return self._attributes[name]
    else:
        raise exceptions.AttributeNotProvided(name)