def get(self, name):
    resolvable, packages, parent, constraint_only = self._collapse().get(self
        .normalize(name), _ResolvedPackages.empty())
    return packages