def typechecked_class(cls, force=False, force_recursive=False):
    return _typechecked_class(cls, set(), force, force_recursive)