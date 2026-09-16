def delegate(from_owner, to_owner, methods):
    for method in methods:
        _delegate(from_owner, to_owner, method)