def is_subtype(type, base):
    assert isinstance(type, basestring)
    assert isinstance(base, basestring)
    return is_derived(type, base)