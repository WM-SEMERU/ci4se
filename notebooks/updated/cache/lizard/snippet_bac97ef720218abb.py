def _on_ready_read(self):
    while self.bytesAvailable():
        if not self._header_complete:
            self._read_header()
        else:
            self._read_payload()