def _validate_granttype(self, path, obj, _):
    errs = []
    if not obj.implicit and not obj.authorization_code:
        errs.append('Either implicit or authorization_code should be defined.')
    return path, obj.__class__.__name__, errs