def _ParseHeader(self, parser_mediator, structure):
    _, month, day, hours, minutes, seconds, year = structure.date_time
    month = timelib.MONTH_DICT.get(month.lower(), 0)
    time_elements_tuple = year, month, day, hours, minutes, seconds
    try:
        date_time = dfdatetime_time_elements.TimeElements(time_elements_tuple
            =time_elements_tuple)
        date_time.is_local_time = True
    except ValueError:
        parser_mediator.ProduceExtractionWarning(
            'invalid date time value: {0!s}'.format(structure.date_time))
        return
    self._last_month = month
    event_data = XChatLogEventData()
    if structure.log_action[0] == 'BEGIN':
        self._xchat_year = year
        event_data.text = 'XChat start logging'
    elif structure.log_action[0] == 'END':
        self._xchat_year = None
        event_data.text = 'XChat end logging'
    else:
        logger.debug('Unknown log action: {0:s}.'.format(' '.join(structure
            .log_action)))
        return
    event = time_events.DateTimeValuesEvent(date_time, definitions.
        TIME_DESCRIPTION_ADDED, time_zone=parser_mediator.timezone)
    parser_mediator.ProduceEventWithEventData(event, event_data)