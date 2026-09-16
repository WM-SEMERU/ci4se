def _ParsePage(self, parser_mediator, file_offset, page_data):
    page_header_map = self._GetDataTypeMap('binarycookies_page_header')
    try:
        page_header = self._ReadStructureFromByteStream(page_data,
            file_offset, page_header_map)
    except (ValueError, errors.ParseError) as exception:
        raise errors.ParseError(
            'Unable to map page header data at offset: 0x{0:08x} with error: {1!s}'
            .format(file_offset, exception))
    for record_offset in page_header.offsets:
        if parser_mediator.abort:
            break
        self._ParseRecord(parser_mediator, page_data, record_offset)