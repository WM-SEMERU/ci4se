def ParseFileObject(self, parser_mediator, file_object):
    file_offset = file_object.get_offset()
    file_size = file_object.get_size()
    while file_offset < file_size:
        try:
            self._ParseRecord(parser_mediator, file_object)
        except errors.ParseError as exception:
            if file_offset == 0:
                raise errors.UnableToParseFile(
                    'Unable to parse first event record with error: {0!s}'.
                    format(exception))
        file_offset = file_object.get_offset()