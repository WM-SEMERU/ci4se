def resolve_node(self, node=None, resolved=None, seen=None):
    if seen is None:
        seen = []
    if resolved is None:
        resolved = []
    if node is None:
        dependencies = sorted(self._nodes.keys())
    else:
        dependencies = self._nodes[node]
        seen.append(node)
    for dependency in dependencies:
        if dependency in resolved:
            continue
        if dependency in seen:
            raise Exception('Circular dependency %s > %s', str(node), str(
                dependency))
        self.resolve_node(dependency, resolved, seen)
    if node is not None:
        resolved.append(node)
    return resolved