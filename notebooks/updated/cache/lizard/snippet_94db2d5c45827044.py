def load_mirteFile(path, m, logger=None):
    l = logging.getLogger('load_mirteFile') if logger is None else logger
    had = set()
    for name, path, d in walk_mirteFiles(path, logger):
        if os.path.realpath(path) in m.loaded_mirteFiles:
            continue
        identifier = name
        if name in had:
            identifier = path
        else:
            had.add(name)
        l.info('loading %s' % identifier)
        m.loaded_mirteFiles.add(os.path.realpath(path))
        _load_mirteFile(d, m)