def _render_frame(self):
    frame = self.frame()
    output = '\r{0}'.format(frame)
    self.clear()
    try:
        self._stream.write(output)
    except UnicodeEncodeError:
        self._stream.write(encode_utf_8_text(output))