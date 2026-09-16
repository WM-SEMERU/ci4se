def to_dictionary(self):
    j = {}
    for p in self.properties:
        try:
            v = getattr(self, p)
        except AttributeError:
            continue
        if v is not None:
            if p == 't':
                j[p] = getattr(self, p).isoformat()
            else:
                j[p] = getattr(self, p)
    return j