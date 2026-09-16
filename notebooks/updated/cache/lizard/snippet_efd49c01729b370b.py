def get_module_owned_functions(module):
    import utool as ut
    list_ = []
    for key, val in ut.iter_module_doctestable(module):
        belongs = False
        if hasattr(val, '__module__'):
            belongs = val.__module__ == module.__name__
        elif hasattr(val, 'func_globals'):
            belongs = val.func_globals['__name__'] == module.__name__
        if belongs:
            list_.append(val)
    return list_