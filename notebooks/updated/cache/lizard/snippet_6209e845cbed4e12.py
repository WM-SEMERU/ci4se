def real_name(self, asname):
    for name, _asname in self.names:
        if name == '*':
            return asname
        if not _asname:
            name = name.split('.', 1)[0]
            _asname = name
        if asname == _asname:
            return name
    raise exceptions.AttributeInferenceError(
        'Could not find original name for {attribute} in {target!r}',
        target=self, attribute=asname)