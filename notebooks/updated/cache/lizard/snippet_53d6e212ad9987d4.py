def aliased(aliased_class):
    original_methods = aliased_class.__dict__.copy()
    for name, method in original_methods.items():
        if hasattr(method, '_aliases'):
            for alias in (method._aliases - set(original_methods)):
                setattr(aliased_class, alias, method)
    return aliased_class