def ParseFileObject(self, parser_mediator, file_object):
    file_size = file_object.get_size()
    file_header_map = self._GetDataTypeMap('rp_log_file_header')
    try:
        file_header, _ = self._ReadStructureFromFileObject(file_object, 0,
            file_header_map)
    except (ValueError, errors.ParseError) as exception:
        raise errors.UnableToParseFile(
            'Unable to parse file header with error: {0!s}'.format(exception))
    file_footer_map = self._GetDataTypeMap('rp_log_file_footer')
    file_footer_offset = file_size - file_footer_map.GetByteSize()
    try:
        file_footer, _ = self._ReadStructureFromFileObject(file_object,
            file_footer_offset, file_footer_map)
    except (ValueError, errors.ParseError) as exception:
        parser_mediator.ProduceExtractionWarning(
            'unable to parse file footer with error: {0!s}'.format(exception))
        return
    description = file_header.description.rstrip('\x00')
    if file_footer.creation_time == 0:
        date_time = dfdatetime_semantic_time.SemanticTime('Not set')
    else:
        date_time = dfdatetime_filetime.Filetime(timestamp=file_footer.
            creation_time)
    event_data = RestorePointEventData()
    event_data.description = description
    event_data.restore_point_event_type = file_header.event_type
    event_data.restore_point_type = file_header.restore_point_type
    event_data.sequence_number = file_header.sequence_number
    event = time_events.DateTimeValuesEvent(date_time, definitions.
        TIME_DESCRIPTION_CREATION)
    parser_mediator.ProduceEventWithEventData(event, event_data)