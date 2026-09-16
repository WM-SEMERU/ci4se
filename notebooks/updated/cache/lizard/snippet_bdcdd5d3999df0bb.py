def init_module(path):
    mod = import_by_path(path)
    if mod is not None and hasattr(mod, 'init'):
        logger.debug('calling init on {0}'.format(mod))
        global PATH
        PATH = path
        mod.init(DictObj(globals()))