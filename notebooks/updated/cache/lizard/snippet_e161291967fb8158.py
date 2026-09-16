def add_deps(self, deps):
    if isinstance(deps, collections.Mapping):
        deps = [Dependency(node, exts) for node, exts in deps.items()]
    if not isinstance(deps, (list, tuple)):
        deps = [deps]
    assert all(isinstance(d, Dependency) for d in deps)
    self._deps.extend(deps)
    if self.is_work:
        for task in self:
            task.add_deps(deps)
    for dep in (d for d in deps if d.node.is_file):
        dep.node.add_filechild(self)