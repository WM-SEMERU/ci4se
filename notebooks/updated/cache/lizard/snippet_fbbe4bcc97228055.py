def WriteHeader(self):
    output_text = self._field_delimiter.join(self._fields)
    output_text = '{0:s}\n'.format(output_text)
    self._output_writer.Write(output_text)