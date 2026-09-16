def _GetStat(self):
    stat_object = super(APFSFileEntry, self)._GetStat()
    stat_object.size = self._fsapfs_file_entry.size
    stat_object.mode = self._fsapfs_file_entry.file_mode & 4095
    stat_object.uid = self._fsapfs_file_entry.owner_identifier
    stat_object.gid = self._fsapfs_file_entry.group_identifier
    stat_object.type = self.entry_type
    stat_object.ino = self._fsapfs_file_entry.identifier
    stat_object.fs_type = 'APFS'
    stat_object.is_allocated = True
    return stat_object