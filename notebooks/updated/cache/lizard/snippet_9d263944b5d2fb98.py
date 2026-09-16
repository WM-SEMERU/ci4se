def func_accepts_var_args(func):
    if six.PY2:
        return inspect.getargspec(func)[1] is not None
    return any(p for p in inspect.signature(func).parameters.values() if p.
        kind == p.VAR_POSITIONAL)