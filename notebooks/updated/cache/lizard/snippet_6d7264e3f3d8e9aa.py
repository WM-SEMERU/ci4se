def _parseline(self, line):
    sline = line.split(SEPARATOR)
    segment = sline[0]
    handlers = {SEGMENT_HEADER: self._handle_header, SEGMENT_EOF: self.
        _handle_eof, SEGMENT_RESULT: self._handle_result_line,
        SEGMENT_OBSERVATION_ORDER: self._handle_new_record}
    handler = handlers.get(segment)
    if handler:
        return handler(sline)
    return 0