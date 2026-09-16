def import_all_modules(package, skip=None, verbose=False, prefix='', depth=0):
    skip = [] if skip is None else skip
    for ff, modname, ispkg in pkgutil.walk_packages(path=package.__path__,
        prefix=prefix, onerror=lambda x: None):
        if ff.path not in package.__path__[0]:
            continue
        if verbose:
            print('\t' * depth, modname)
        if modname in skip:
            if verbose:
                print('\t' * depth, '*Skipping*')
            continue
        module = '%s.%s' % (package.__name__, modname)
        subpackage = importlib.import_module(module)
        if ispkg:
            import_all_modules(subpackage, skip=skip, verbose=verbose,
                depth=depth + 1)