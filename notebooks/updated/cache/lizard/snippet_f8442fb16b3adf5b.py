def strict_deps_for_target(self, target, predicate=None):
    if self._native_build_settings.get_strict_deps_value_for_target(target):
        strict_deps = target.strict_dependencies(DependencyContext())
        if predicate:
            filtered_deps = list(filter(predicate, strict_deps))
        else:
            filtered_deps = strict_deps
        deps = [target] + filtered_deps
    else:
        deps = self.context.build_graph.transitive_subgraph_of_addresses([
            target.address], predicate=predicate)
    deps = filter(predicate, deps)
    return deps