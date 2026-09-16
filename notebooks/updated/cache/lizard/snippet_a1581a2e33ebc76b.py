def _get_properties(self, logical_id):
    if logical_id not in self.by_resource:
        self.by_resource[logical_id] = self.Properties(apis=[],
            binary_media_types=set(), cors=None)
    return self.by_resource[logical_id]