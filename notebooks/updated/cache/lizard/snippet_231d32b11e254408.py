def _ReadLine(self, file_object):
    if len(self._buffer) < self._buffer_size:
        content = file_object.read(self._buffer_size)
        content = content.decode(self._encoding)
        self._buffer = ''.join([self._buffer, content])
    line, new_line, self._buffer = self._buffer.partition('\n')
    if not line and not new_line:
        line = self._buffer
        self._buffer = ''
    self._current_offset += len(line)
    if line.endswith('\r'):
        line = line[:-len('\r')]
    if new_line:
        line = ''.join([line, '\n'])
        self._current_offset += len('\n')
    return line