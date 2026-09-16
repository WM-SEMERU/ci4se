def _detect_type_load_headers(self, stream, statusline=None, known_format=None
    ):
    if known_format != 'arc':
        try:
            rec_headers = self.warc_parser.parse(stream, statusline)
            return 'warc', rec_headers
        except StatusAndHeadersParserException as se:
            if known_format == 'warc':
                msg = 'Invalid WARC record, first line: '
                raise ArchiveLoadFailed(msg + str(se.statusline))
            statusline = se.statusline
            pass
    try:
        rec_headers = self.arc_parser.parse(stream, statusline)
        return self.arc_parser.get_rec_type(), rec_headers
    except StatusAndHeadersParserException as se:
        if known_format == 'arc':
            msg = 'Invalid ARC record, first line: '
        else:
            msg = 'Unknown archive format, first line: '
        raise ArchiveLoadFailed(msg + str(se.statusline))