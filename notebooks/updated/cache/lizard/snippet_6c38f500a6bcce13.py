def remove_declarated(type_):
    type_ = remove_alias(type_)
    if isinstance(type_, cpptypes.elaborated_t):
        type_ = type_.base
    if isinstance(type_, cpptypes.declarated_t):
        type_ = type_.declaration
    return type_