def _ParseRecordLogline(self, parser_mediator, structure):
    date_time = dfdatetime_time_elements.TimeElementsInMilliseconds()
    try:
        datetime_iso8601 = self._GetISO8601String(structure.date_time)
        date_time.CopyFromStringISO8601(datetime_iso8601)
    except ValueError:
        parser_mediator.ProduceExtractionWarning(
            'invalid date time value: {0!s}'.format(structure.date_time))
        return
    event_data = GoogleDriveSyncLogEventData()
    event_data.log_level = structure.log_level
    event_data.pid = structure.pid
    event_data.thread = structure.thread
    event_data.source_code = structure.source_code
    event_data.message = structure.message.replace('\n', ' ')
    event = time_events.DateTimeValuesEvent(date_time, definitions.
        TIME_DESCRIPTION_ADDED)
    parser_mediator.ProduceEventWithEventData(event, event_data)