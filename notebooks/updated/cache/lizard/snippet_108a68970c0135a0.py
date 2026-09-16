def is_union(declaration):
    if not is_class(declaration):
        return False
    decl = class_traits.get_declaration(declaration)
    return decl.class_type == class_declaration.CLASS_TYPES.UNION