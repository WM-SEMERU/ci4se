def _GetDirectory(self):
    if self.entry_type != definitions.FILE_ENTRY_TYPE_DIRECTORY:
        return None
    return APFSContainerDirectory(self._file_system, self.path_spec)