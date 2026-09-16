def __add_flag(rule_or_module, variable_name, condition, values):
    assert isinstance(rule_or_module, basestring)
    assert isinstance(variable_name, basestring)
    assert is_iterable_typed(condition, property_set.PropertySet)
    assert is_iterable(values) and all(isinstance(v, (basestring, type(None
        ))) for v in values)
    f = Flag(variable_name, values, condition, rule_or_module)
    m = __re_first_segment.match(rule_or_module)
    assert m
    module = m.group(1)
    __module_flags.setdefault(module, []).append(f)
    __flags.setdefault(rule_or_module, []).append(f)