def recordDecl(*args):
    kinds = [CursorKind.STRUCT_DECL, CursorKind.UNION_DECL, CursorKind.
        CLASS_DECL, CursorKind.CLASS_TEMPLATE]
    inner = [PredMatcher(is_kind(k)) for k in kinds]
    return allOf(anyOf(*inner), *args)