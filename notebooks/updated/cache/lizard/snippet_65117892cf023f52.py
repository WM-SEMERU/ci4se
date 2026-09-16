def _GetStat(self):
    stat_object = super(ZipFileEntry, self)._GetStat()
    if self._zip_info is not None:
        stat_object.size = getattr(self._zip_info, 'file_size', None)
        if self._external_attributes != 0:
            if self._creator_system == self._CREATOR_SYSTEM_UNIX:
                st_mode = self._external_attributes >> 16
                stat_object.mode = st_mode & 4095
    return stat_object