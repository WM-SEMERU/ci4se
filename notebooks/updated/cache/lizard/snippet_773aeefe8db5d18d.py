def get_type(name, library):
    if name == None:
        raise Exception('Class name cannot be null')
    if library == None:
        raise Exception('Module name cannot be null')
    try:
        module = importlib.import_module(library)
        return getattr(module, name)
    except:
        return None