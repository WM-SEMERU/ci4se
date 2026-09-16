def inject_dependency(self, dependency_address):
    self._build_graph.inject_dependency(dependent=self.address, dependency=
        dependency_address)

    def invalidate_dependee(dependee):
        dependee.mark_transitive_invalidation_hash_dirty()
    self._build_graph.walk_transitive_dependee_graph([self.address], work=
        invalidate_dependee)