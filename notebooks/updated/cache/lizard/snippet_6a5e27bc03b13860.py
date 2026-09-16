def read(self):
    if self._output_buffer:
        b, self._output_buffer = self._output_buffer[0:1], self._output_buffer[
            1:]
        return b
    return b''