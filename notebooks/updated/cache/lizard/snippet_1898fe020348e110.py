def is_pointer(type_):
    return does_match_definition(type_, cpptypes.pointer_t, (cpptypes.
        const_t, cpptypes.volatile_t)) or does_match_definition(type_,
        cpptypes.pointer_t, (cpptypes.volatile_t, cpptypes.const_t))