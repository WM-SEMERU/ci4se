def is_copy_constructor(constructor):
    assert isinstance(constructor, calldef_members.constructor_t)
    args = constructor.arguments
    parent = constructor.parent
    if len(args) != 1:
        return False
    arg = args[0]
    if not isinstance(arg.decl_type, cpptypes.compound_t):
        return False
    if not type_traits.is_reference(arg.decl_type):
        return False
    if not type_traits.is_const(arg.decl_type.base):
        return False
    un_aliased = type_traits.remove_alias(arg.decl_type.base)
    if not isinstance(un_aliased.base, cpptypes.declarated_t):
        return False
    return id(un_aliased.base.declaration) == id(parent)