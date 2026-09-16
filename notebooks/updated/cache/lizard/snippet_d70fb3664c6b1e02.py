def Read(self):
    input_string = self._file_object.readline()
    if isinstance(input_string, py2to3.BYTES_TYPE):
        try:
            input_string = codecs.decode(input_string, self._encoding, self
                ._errors)
        except UnicodeDecodeError:
            if self._errors == 'strict':
                logging.error(
                    'Unable to properly read input due to encoding error. Switching to error tolerant encoding which can result in non Basic Latin (C0) characters to be replaced with "?" or "\\ufffd".'
                    )
                self._errors = 'replace'
            input_string = codecs.decode(input_string, self._encoding, self
                ._errors)
    return input_string