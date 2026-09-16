def aliased(aliased_class):
    original_methods = aliased_class.__dict__.copy()
    original_methods_set = set(original_methods)
    for name, method in original_methods.items():
        aliases = None
        if isinstance(method, property) and hasattr(method.fget, '_aliases'):
            aliases = method.fget._aliases
        elif hasattr(method, '_aliases'):
            aliases = method._aliases
        if aliases:
            for alias in (aliases - original_methods_set):
                setattr(aliased_class, alias, method)
    return aliased_class