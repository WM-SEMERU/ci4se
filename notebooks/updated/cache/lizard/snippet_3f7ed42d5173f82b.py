def _getID(self):
    id = []
    for key in self._sqlPrimary:
        value = self.__dict__[key]
        if isinstance(value, Forgetter):
            if value._new:
                value.save()
            try:
                value, = value._getID()
            except:
                raise (
                    'Unsupported: Part %s of %s primary key is a reference to %s, with multiple-primary-key %s '
                     % (key, self.__class__, value.__class__, value))
        id.append(value)
    return id