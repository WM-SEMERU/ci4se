def deep_copy(self):
    return OrdinalColumn(self.arr, metadata=self.metadata, name=self.name,
        missing_id=self._missing_id, substitute=True, groupings=self.
        _groupings, weights=self.weights)