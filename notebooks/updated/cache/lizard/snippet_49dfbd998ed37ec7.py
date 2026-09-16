def equal(value_a, value_b):
    if not isinstance(value_a, HasProperties) or not isinstance(value_b,
        HasProperties):
        return value_a == value_b
    if getattr(value_a, '_testing_equality', False):
        return False
    value_a._testing_equality = True
    try:
        if value_a is value_b:
            return True
        if value_a.__class__ is not value_b.__class__:
            return False
        for prop in itervalues(value_a._props):
            prop_a = getattr(value_a, prop.name)
            prop_b = getattr(value_b, prop.name)
            if prop_a is None and prop_b is None:
                continue
            if prop_a is not None and prop_b is not None and prop.equal(prop_a,
                prop_b):
                continue
            return False
        return True
    finally:
        value_a._testing_equality = False