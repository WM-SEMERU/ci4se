def append(self, entity, name='pers'):
    e = map(lambda s: s.lower(), entity.split(' ') + [name])
    self.setdefault(e[0], []).append(e)