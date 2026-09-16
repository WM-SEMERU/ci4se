def ExtractEvents(self, parser_mediator, registry_key, **kwargs):
    shutdown_value = registry_key.GetValueByName('ShutdownTime')
    if not shutdown_value:
        return
    try:
        date_time = self._ParseFiletime(shutdown_value.data)
    except errors.ParseError as exception:
        parser_mediator.ProduceExtractionWarning(
            'unable to determine shutdown timestamp with error: {0!s}'.
            format(exception))
        return
    if not date_time:
        date_time = dfdatetime_semantic_time.SemanticTime('Not set')
    event_data = ShutdownWindowsRegistryEventData()
    event_data.key_path = registry_key.path
    event_data.offset = shutdown_value.offset
    event_data.value_name = shutdown_value.name
    event = time_events.DateTimeValuesEvent(date_time, definitions.
        TIME_DESCRIPTION_LAST_SHUTDOWN)
    parser_mediator.ProduceEventWithEventData(event, event_data)