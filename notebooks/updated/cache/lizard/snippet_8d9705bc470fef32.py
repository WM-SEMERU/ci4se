def parse_with_objects(code, var, **kwargs):
    deps = {}
    for key, value in kwargs.items():
        if isinstance(value, _compat.integer_types):
            value = str(value)
        if _compat.PY3:
            if value is None:
                value = str(value)
        if not isinstance(value, _compat.string_types) and not isinstance(value
            , CodeBlock):
            new_var = var(value)
            deps[new_var] = value
            kwargs[key] = new_var
    block, var = parse_code(code, var, **kwargs)
    for key, dep in _compat.iteritems(deps):
        block.add_dependency(key, dep)
    return block, var