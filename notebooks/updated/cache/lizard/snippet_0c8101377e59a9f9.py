def isimplementation(obj, interfaces):
    if not inspect.isclass(obj):
        isimplementation(obj.__class__, interfaces)
    if not isinstance(interfaces, collections.Iterable):
        interfaces = [interfaces]
    return frozenset(interfaces).issubset(get_implemented_interfaces(obj))