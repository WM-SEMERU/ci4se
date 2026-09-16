def expand_dependencies_section(section, kwargs):
    deps = []
    for dep in section:
        for dep_type, dep_list in dep.items():
            if dep_type in ['call', 'use']:
                deps.extend(Command(dep_type, dep_list, kwargs).run())
            elif dep_type.startswith('if ') or dep_type == 'else':
                deps.append({dep_type: expand_dependencies_section(dep_list,
                    kwargs)})
            else:
                deps.append({dep_type: dep_list})
    return deps