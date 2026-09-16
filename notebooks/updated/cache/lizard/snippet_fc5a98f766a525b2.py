def import_name(name, default_ns=None):
    if '.' not in name:
        if default_ns is None:
            return importlib.import_module(name)
        else:
            name = default_ns + '.' + name
    module_name, object_name = name.rsplit('.', 1)
    module = importlib.import_module(module_name)
    return getattr(module, object_name)