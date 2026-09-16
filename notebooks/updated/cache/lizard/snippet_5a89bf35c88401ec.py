def ExtractEvents(self, parser_mediator, registry_key, **kwargs):
    values_dict = {}
    for registry_value in registry_key.GetValues():
        if not registry_value.name or not registry_value.data:
            continue
        if registry_value.name == 'UpdateKey':
            self._ParseUpdateKeyValue(parser_mediator, registry_value,
                registry_key.path)
        else:
            values_dict[registry_value.name] = registry_value.GetDataAsObject()
    event_data = windows_events.WindowsRegistryEventData()
    event_data.key_path = registry_key.path
    event_data.offset = registry_key.offset
    event_data.regvalue = values_dict
    event_data.source_append = self._SOURCE_APPEND
    event_data.urls = self.URLS
    event = time_events.DateTimeValuesEvent(registry_key.last_written_time,
        definitions.TIME_DESCRIPTION_WRITTEN)
    parser_mediator.ProduceEventWithEventData(event, event_data)