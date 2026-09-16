def GetParentFileEntry(self):
    volume_index = apfs_helper.APFSContainerPathSpecGetVolumeIndex(self.
        path_spec)
    if volume_index is None:
        return None
    return self._file_system.GetRootFileEntry()