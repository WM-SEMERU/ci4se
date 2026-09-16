def maybe_raise(cls, error_type, ignores=None):
    ignores = set(ignores or [])
    ignores.add(ErrorType.Ok)
    if error_type not in ignores:
        raise LibError(error_type)