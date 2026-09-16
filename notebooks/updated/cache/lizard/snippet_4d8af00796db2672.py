def _required_args(fn):
    spec = getargspec(fn)
    if not spec.defaults:
        return []
    arg_names = spec.args[-len(spec.defaults):]
    return [name for name, val in zip(arg_names, spec.defaults) if val is
        REQUIRED_ARG]