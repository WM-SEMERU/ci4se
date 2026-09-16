def slurp_properties(source, destination, ignore=[], srckeys=None):
    if srckeys is None:
        srckeys = source.__all__
    destination.update(dict([(name, getattr(source, name)) for name in
        srckeys if not (name.startswith('__') or name in ignore)]))