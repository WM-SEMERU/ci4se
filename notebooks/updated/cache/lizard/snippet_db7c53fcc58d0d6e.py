def import_submodules(module):
    submodules = {}
    for loader, name, ispkg in pkgutil.iter_modules(module.__path__, module
        .__name__ + '.'):
        try:
            submodule = import_module(name)
        except ImportError as e:
            logging.warning('Error importing %s', name)
            logging.exception(e)
        else:
            parent, child = name.rsplit('.', 1)
            submodules[child] = submodule
    return submodules