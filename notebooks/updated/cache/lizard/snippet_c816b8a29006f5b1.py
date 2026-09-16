def _rpc_metadata(self):
    if self._rpc_metadata_internal is None:
        self._rpc_metadata_internal = _helpers.metadata_with_prefix(self.
            _database_string)
    return self._rpc_metadata_internal