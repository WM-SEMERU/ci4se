def _GetLink(self):
    if self._link is None:
        self._link = ''
        if self.entry_type != definitions.FILE_ENTRY_TYPE_LINK:
            return self._link
        cpio_archive_file = self._file_system.GetCPIOArchiveFile()
        link_data = cpio_archive_file.ReadDataAtOffset(self.
            _cpio_archive_file_entry.data_offset, self.
            _cpio_archive_file_entry.data_size)
        self._link = link_data.decode('ascii')
    return self._link