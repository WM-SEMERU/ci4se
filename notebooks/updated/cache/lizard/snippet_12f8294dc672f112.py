def _finalized(self):
    return len(self._finalized_dependencies) >= self.dependency_count and len(
        self._enqueued_dependencies) >= self.dependency_count