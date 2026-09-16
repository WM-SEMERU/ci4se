def i_depend_on_them(decl):
    to_be_included = set()
    for dependency_info in get_dependencies_from_decl(decl):
        for ddecl in dependency_info.find_out_depend_on_it_declarations():
            if ddecl:
                to_be_included.add(ddecl)
    if isinstance(decl.parent, class_declaration.class_t):
        to_be_included.add(decl.parent)
    return to_be_included