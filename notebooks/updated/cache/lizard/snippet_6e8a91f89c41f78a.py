def _GetStat(self):
    stat_object = super(GzipFileEntry, self)._GetStat()
    if self._gzip_file:
        stat_object.size = self._gzip_file.uncompressed_data_size
    return stat_object