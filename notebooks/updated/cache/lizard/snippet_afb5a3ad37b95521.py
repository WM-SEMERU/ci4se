def load(source, semi=None):
    if hasattr(source, 'read'):
        return _load(source, semi)
    else:
        with open(source, 'r') as fh:
            return _load(fh, semi)