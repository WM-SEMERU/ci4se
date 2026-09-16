def _ProduceEvent(self, parser_mediator, event_data, properties,
    property_name, timestamp_description, error_description):
    time_string = properties.get(property_name, None)
    if not time_string:
        return
    date_time = dfdatetime_time_elements.TimeElements()
    try:
        date_time.CopyFromStringISO8601(time_string)
        event = time_events.DateTimeValuesEvent(date_time,
            timestamp_description)
        parser_mediator.ProduceEventWithEventData(event, event_data)
    except ValueError as exception:
        parser_mediator.ProduceExtractionWarning(
            'unsupported {0:s}: {1:s} with error: {2!s}'.format(
            error_description, time_string, exception))