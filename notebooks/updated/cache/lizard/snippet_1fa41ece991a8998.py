def field(type=PFIELD_NO_TYPE, invariant=PFIELD_NO_INVARIANT, initial=
    PFIELD_NO_INITIAL, mandatory=False, factory=PFIELD_NO_FACTORY,
    serializer=PFIELD_NO_SERIALIZER):
    if isinstance(type, (list, set, tuple)):
        types = set(maybe_parse_many_user_types(type))
    else:
        types = set(maybe_parse_user_type(type))
    invariant_function = wrap_invariant(invariant
        ) if invariant != PFIELD_NO_INVARIANT and callable(invariant
        ) else invariant
    field = _PField(type=types, invariant=invariant_function, initial=
        initial, mandatory=mandatory, factory=factory, serializer=serializer)
    _check_field_parameters(field)
    return field