def GetFileEntryByPathSpec(self, path_spec):
    row_index = getattr(path_spec, 'row_index', None)
    row_condition = getattr(path_spec, 'row_condition', None)
    if row_index is None and row_condition is None:
        return sqlite_blob_file_entry.SQLiteBlobFileEntry(self.
            _resolver_context, self, path_spec, is_root=True, is_virtual=True)
    return sqlite_blob_file_entry.SQLiteBlobFileEntry(self.
        _resolver_context, self, path_spec)