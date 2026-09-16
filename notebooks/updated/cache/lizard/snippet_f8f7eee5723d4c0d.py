def register_module(module=None):
    global REGISTERED_MODULES
    if module is None:
        module = sys.modules.get(inspect.currentframe().f_back.f_globals[
            '__name__'])
    REGISTERED_MODULES.add(module)
    return True