def _resolve_deps(self, depmap):
    deps = defaultdict(lambda : OrderedSet())
    for category, depspecs in depmap.items():
        dependencies = deps[category]
        for depspec in depspecs:
            dep_address = Address.parse(depspec)
            try:
                self.context.build_graph.maybe_inject_address_closure(
                    dep_address)
                dependencies.add(self.context.build_graph.get_target(
                    dep_address))
            except AddressLookupError as e:
                raise AddressLookupError('{}\n  referenced from {} scope'.
                    format(e, self.options_scope))
    return deps