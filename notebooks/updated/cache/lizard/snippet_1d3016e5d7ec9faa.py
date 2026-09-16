def import_(module_name, backport=False):
    import importlib
    if PY3:
        return __import__(module_name)
    else:
        if backport:
            prefix = 'future.backports'
        else:
            prefix = 'future.moves'
        parts = prefix.split('.') + module_name.split('.')
        modules = []
        for i, part in enumerate(parts):
            sofar = '.'.join(parts[:i + 1])
            modules.append(importlib.import_module(sofar))
        for i, part in reversed(list(enumerate(parts))):
            if i == 0:
                break
            setattr(modules[i - 1], part, modules[i])
        return modules[2]