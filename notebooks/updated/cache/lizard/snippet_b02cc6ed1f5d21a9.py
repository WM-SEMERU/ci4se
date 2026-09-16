def list_to_scope(scope):
    if isinstance(scope, unicode_type) or scope is None:
        return scope
    elif isinstance(scope, (set, tuple, list)):
        return ' '.join([unicode_type(s) for s in scope])
    else:
        raise ValueError(
            'Invalid scope (%s), must be string, tuple, set, or list.' % scope)