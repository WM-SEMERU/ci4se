def pack(self, namedstruct):
    elements = []
    t = namedstruct._target
    for p in self.properties:
        v = t
        for sp in p[0]:
            v = getattr(v, sp)
        if len(p) > 1:
            elements.extend(v[0:p[1]])
        else:
            elements.append(v)
    return self.struct.pack(*elements)