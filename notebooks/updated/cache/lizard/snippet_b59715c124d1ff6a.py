def mk_package(contents):
    package = contents.get('package', None)
    description = contents.get('description', None)
    include = contents.get('include', [])
    definitions = contents.get('definitions', [])
    resolved = [mk_definition(defn) for defn in definitions]
    return sbp.PackageSpecification(identifier=package, description=
        description, includes=include, definitions=resolved, render_source=
        contents.get('render_source', True), stable=contents.get('stable',
        False), public=contents.get('public', True))