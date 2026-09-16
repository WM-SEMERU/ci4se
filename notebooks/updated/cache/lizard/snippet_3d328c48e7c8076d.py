def scope_to_list(scope):
    if isinstance(scope, (tuple, list, set)):
        return [unicode_type(s) for s in scope]
    elif scope is None:
        return None
    else:
        return scope.strip().split(' ')