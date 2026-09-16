def as_dict(self):
    d = {'@module': self.__class__.__module__, '@class': self.__class__.
        __name__, 'structure': self.structure.as_dict(), 'frequencies':
        list(self.frequencies), 'densities': list(self.densities), 'pdos': []}
    if len(self.pdos) > 0:
        for at in self.structure:
            d['pdos'].append(list(self.pdos[at]))
    return d