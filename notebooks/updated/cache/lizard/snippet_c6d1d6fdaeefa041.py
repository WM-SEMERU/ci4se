def value(self):
    val = {}
    for k in self.__allowed_keys:
        v = getattr(self, '_' + k)
        if v is not None:
            val[k] = v
    return val