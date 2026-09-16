def find(self, package, **kwargs):
    spec = find_spec(package)
    if spec is None:
        return None
    limit = []
    if '.' in package:
        package, limit = package.split('.', 1)
        limit = [limit]
        spec = find_spec(package)
    if spec is not None:
        if spec.submodule_search_locations:
            path = spec.submodule_search_locations[0]
        elif spec.origin and spec.origin != 'built-in':
            path = spec.origin
        else:
            return None
        return PackageSpec(spec.name, path, limit)
    return None