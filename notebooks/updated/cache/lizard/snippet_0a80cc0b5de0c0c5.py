def align_after(self, offset):
    f = self.reader
    if offset <= 0:
        f.seek(0)
        self._block_count = 0
        self._read_header()
        return
    sm = self.sync_marker
    sml = len(sm)
    pos = offset
    while pos < self.file_length - sml:
        f.seek(pos)
        data = f.read(self.FORWARD_WINDOW_SIZE)
        sync_offset = data.find(sm)
        if sync_offset > -1:
            f.seek(pos + sync_offset)
            self._block_count = 0
            return
        pos += len(data)