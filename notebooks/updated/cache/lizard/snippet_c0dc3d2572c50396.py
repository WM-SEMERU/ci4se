def replace_built(self, built_packages):

    def map_packages(resolved_packages):
        packages = OrderedSet(built_packages.get(p, p) for p in
            resolved_packages.packages)
        return _ResolvedPackages(resolved_packages.resolvable, packages,
            resolved_packages.parent, resolved_packages.constraint_only)
    return _ResolvableSet([map_packages(rp) for rp in self.__tuples])