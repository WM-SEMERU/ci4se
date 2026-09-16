def _define_fixed(wrapped, callable_):
    is_class = inspect.isclass(wrapped)
    style = callable_._splpy_style if hasattr(callable_, '_splpy_style'
        ) else wrapped._splpy_style
    if style == 'dictionary':
        return -1
    fixed_count = 0
    if style == 'tuple':
        sig = _inspect.signature(callable_)
        pmds = sig.parameters
        itpmds = iter(pmds)
        if is_class:
            next(itpmds)
        for pn in itpmds:
            param = pmds[pn]
            if param.kind == _inspect.Parameter.POSITIONAL_OR_KEYWORD:
                fixed_count += 1
            if param.kind == _inspect.Parameter.VAR_POSITIONAL:
                fixed_count = -1
                break
            if param.kind == _inspect.Parameter.VAR_KEYWORD:
                break
    return fixed_count