def import_models(module):
    try:
        module = importlib.import_module('{0}.models'.format(module))
    except ImportError:
        return []
    else:
        clsmembers = inspect.getmembers(module, lambda member: inspect.
            isclass(member) and member.__module__ == module.__name__)
        return [kls for name, kls in clsmembers]