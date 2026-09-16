def refine(properties, requirements):
    assert is_iterable_typed(properties, Property)
    assert is_iterable_typed(requirements, Property)
    result = set()
    required = {}
    for r in requirements:
        if not r.condition:
            required[r.feature] = r
    for p in properties:
        if p.condition:
            result.add(p)
        elif p.feature.free:
            result.add(p)
        elif p.feature in required:
            result.add(required[p.feature])
        else:
            result.add(p)
    return sequence.unique(list(result) + requirements)