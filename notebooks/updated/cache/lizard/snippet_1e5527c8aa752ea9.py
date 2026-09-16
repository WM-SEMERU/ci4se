def _ParseLogLine(self, parser_mediator, structure):
    if structure.date_time:
        time_elements_tuple = structure.date_time
    elif structure.date and structure.time:
        year, month, day_of_month = structure.date
        hours, minutes, seconds = structure.time
        time_elements_tuple = (year, month, day_of_month, hours, minutes,
            seconds)
    elif structure.time:
        hours, minutes, seconds = structure.time
        time_elements_tuple = (self._year, self._month, self._day_of_month,
            hours, minutes, seconds)
    else:
        parser_mediator.ProduceExtractionWarning('missing date and time values'
            )
        return
    try:
        date_time = dfdatetime_time_elements.TimeElements(time_elements_tuple
            =time_elements_tuple)
    except ValueError:
        parser_mediator.ProduceExtractionWarning(
            'invalid date time value: {0!s}'.format(time_elements_tuple))
        return
    event_data = IISEventData()
    for key, value in iter(structure.items()):
        if key in ('date', 'date_time', 'time') or value == '-':
            continue
        if isinstance(value, pyparsing.ParseResults):
            value = ''.join(value)
        setattr(event_data, key, value)
    event = time_events.DateTimeValuesEvent(date_time, definitions.
        TIME_DESCRIPTION_WRITTEN)
    parser_mediator.ProduceEventWithEventData(event, event_data)