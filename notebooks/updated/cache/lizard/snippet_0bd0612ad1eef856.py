def is_calldef_pointer(type_):
    if not is_pointer(type_):
        return False
    nake_type = remove_alias(type_)
    nake_type = remove_cv(nake_type)
    return isinstance(nake_type, cpptypes.compound_t) and isinstance(nake_type
        .base, cpptypes.calldef_type_t)