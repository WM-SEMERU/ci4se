def importer(name, extensions=None, sniff=None):
    name = name.lower()
    if name in importers:
        raise ValueError(
            'An importer for type %s already exists; see forget_importer' %
            name)
    if extensions is None:
        extensions = ()
    elif pimms.is_str(extensions):
        extensions,
    else:
        extensions = tuple(extensions)

    def _importer(f):
        global importers
        importers = importers.set(name, (f, extensions, sniff))
        setattr(load, name, f)
        return f
    return _importer