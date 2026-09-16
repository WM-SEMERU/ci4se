def evaluate_conditionals_in_context(properties, context):
    if __debug__:
        from .property_set import PropertySet
        assert is_iterable_typed(properties, Property)
        assert isinstance(context, PropertySet)
    base = []
    conditional = []
    for p in properties:
        if p.condition:
            conditional.append(p)
        else:
            base.append(p)
    result = base[:]
    for p in conditional:
        if all(x in context for x in p.condition):
            result.append(Property(p.feature, p.value))
    return result