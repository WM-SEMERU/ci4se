def map_ormclass(self, name):
    try:
        self._mapped[name] = getattr(self._pkg, self._prefix + name)
    except AttributeError:
        print('Warning: Relation %s does not exist.' % name)