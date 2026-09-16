def create(raw_properties=[]):
    assert is_iterable_typed(raw_properties, property.Property
        ) or is_iterable_typed(raw_properties, basestring)
    if len(raw_properties) > 0 and isinstance(raw_properties[0], property.
        Property):
        x = raw_properties
    else:
        x = [property.create_from_string(ps) for ps in raw_properties]
    x = sorted(set(x), key=lambda p: (p.feature.name, p.value, p.condition))
    key = tuple(p.id for p in x)
    if key not in __cache:
        __cache[key] = PropertySet(x)
    return __cache[key]