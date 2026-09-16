def resolve_deps(self, obj):
    deps = self.get_deps(obj)
    return list(self.iresolve(*deps))