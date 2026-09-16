def _is_final(meta, arg):
    if inspect.isclass(arg) and not isinstance(arg, ObjectMetaclass):
        return False
    from taipan.objective.modifiers import _WrappedMethod
    if isinstance(arg, _WrappedMethod):
        arg = arg.method
    return getattr(arg, '__final__', False)