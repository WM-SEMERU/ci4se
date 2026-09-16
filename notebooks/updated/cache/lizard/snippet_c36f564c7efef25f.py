def pmap_field(key_type, value_type, optional=False, invariant=
    PFIELD_NO_INVARIANT):
    TheMap = _make_pmap_field_type(key_type, value_type)
    if optional:

        def factory(argument):
            if argument is None:
                return None
            else:
                return TheMap.create(argument)
    else:
        factory = TheMap.create
    return field(mandatory=True, initial=TheMap(), type=optional_type(
        TheMap) if optional else TheMap, factory=factory, invariant=invariant)