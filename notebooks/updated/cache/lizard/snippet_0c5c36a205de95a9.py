def GetFileEntryByPathSpec(self, path_spec):
    fsapfs_file_entry = None
    location = getattr(path_spec, 'location', None)
    identifier = getattr(path_spec, 'identifier', None)
    if (location == self.LOCATION_ROOT or identifier == self.
        ROOT_DIRECTORY_IDENTIFIER):
        fsapfs_file_entry = self._fsapfs_volume.get_root_directory()
        return apfs_file_entry.APFSFileEntry(self._resolver_context, self,
            path_spec, fsapfs_file_entry=fsapfs_file_entry, is_root=True)
    try:
        if identifier is not None:
            fsapfs_file_entry = (self._fsapfs_volume.
                get_file_entry_by_identifier(identifier))
        elif location is not None:
            fsapfs_file_entry = self._fsapfs_volume.get_file_entry_by_path(
                location)
    except IOError as exception:
        raise errors.BackEndError(exception)
    if fsapfs_file_entry is None:
        return None
    return apfs_file_entry.APFSFileEntry(self._resolver_context, self,
        path_spec, fsapfs_file_entry=fsapfs_file_entry)