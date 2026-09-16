def _handle_lines(self):
    while b'\xdd' in self._buffer:
        linebuf, self._buffer = self._buffer.rsplit(b'\xdd', 1)
        line = linebuf[-19:]
        self._buffer += linebuf[:-19]
        if self._valid_packet(line):
            self._handle_raw_packet(line)
        else:
            self.logger.warning('dropping invalid data: %s', binascii.
                hexlify(line))