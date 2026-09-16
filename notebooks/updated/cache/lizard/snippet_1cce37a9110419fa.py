def dependents(self):
    return [self._build_graph.get_target(dep_address) for dep_address in
        self._build_graph.dependents_of(self.address)]