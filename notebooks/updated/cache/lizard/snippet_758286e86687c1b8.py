def import_module(name):
    parts = name.split('.')
    path = None
    module_name = ''
    fhandle = None
    for index, part in enumerate(parts):
        module_name = part if index == 0 else '%s.%s' % (module_name, part)
        path = [path] if path is not None else path
        try:
            fhandle, path, descr = imp.find_module(part, path)
            if module_name in sys.modules:
                mod = sys.modules[module_name]
            else:
                mod = imp.load_module(module_name, fhandle, path, descr)
        finally:
            if fhandle:
                fhandle.close()
    return mod