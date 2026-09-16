def _WriteHeader(self, output_writer):
    header_string = ''
    if self._title:
        header_string = ' {0:s} '.format(self._title)
    header_string = self._HEADER_FORMAT_STRING.format(header_string)
    output_writer.Write(header_string)