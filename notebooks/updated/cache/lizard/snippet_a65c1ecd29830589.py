def ParseFileObject(self, parser_mediator, file_object):
    file_offset = 0
    file_size = file_object.get_size()
    record_map = self._GetDataTypeMap('pls_recall_record')
    while file_offset < file_size:
        try:
            pls_record, record_data_size = self._ReadStructureFromFileObject(
                file_object, file_offset, record_map)
        except (ValueError, errors.ParseError) as exception:
            if file_offset == 0:
                raise errors.UnableToParseFile('Unable to parse first record.')
            parser_mediator.ProduceExtractionWarning(
                'unable to parse record at offset: 0x{0:08x} with error: {1!s}'
                .format(file_offset, exception))
            break
        if file_offset == 0 and not self._VerifyRecord(pls_record):
            raise errors.UnableToParseFile(
                'Verification of first record failed.')
        event_data = PlsRecallEventData()
        event_data.database_name = pls_record.database_name.rstrip('\x00')
        event_data.sequence_number = pls_record.sequence_number
        event_data.offset = file_offset
        event_data.query = pls_record.query.rstrip('\x00')
        event_data.username = pls_record.username.rstrip('\x00')
        date_time = dfdatetime_delphi_date_time.DelphiDateTime(timestamp=
            pls_record.last_written_time)
        event = time_events.DateTimeValuesEvent(date_time, definitions.
            TIME_DESCRIPTION_WRITTEN)
        parser_mediator.ProduceEventWithEventData(event, event_data)
        file_offset += record_data_size