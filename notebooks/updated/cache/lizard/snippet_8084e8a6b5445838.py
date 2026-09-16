def does_match_definition(given, main, secondary):
    assert isinstance(secondary, tuple)
    assert len(secondary) == 2
    types = decompose_type(given)
    if isinstance(types[0], main):
        return True
    if len(types) >= 2:
        cond1 = isinstance(types[0], main)
        cond2 = isinstance(types[1], secondary)
        cond3 = isinstance(types[1], main)
        cond4 = isinstance(types[0], secondary)
        if cond1 and cond2 or cond3 and cond4:
            return True
        if len(types) >= 3:
            classes = set([tp.__class__ for tp in types[:3]])
            desired = set([main] + list(secondary))
            diff = classes.symmetric_difference(desired)
            if not diff:
                return True
            if len(diff) == 2:
                items = list(diff)
                return issubclass(items[0], items[1]) or issubclass(items[1
                    ], items[0])
            return False
    else:
        return False