def root_manifest_id(self, root_manifest_id):
    if root_manifest_id is not None and len(root_manifest_id) > 32:
        raise ValueError(
            'Invalid value for `root_manifest_id`, length must be less than or equal to `32`'
            )
    self._root_manifest_id = root_manifest_id