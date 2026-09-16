def _getModuleMember(self, dotted_name, member):
    try:
        mod = importlib.import_module(dotted_name)
    except ImportError:
        return None
    members = dict(inspect.getmembers(mod))
    return members.get(member)