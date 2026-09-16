def ParseContainersTable(self, parser_mediator, database=None, table=None,
    **unused_kwargs):
    if database is None:
        raise ValueError('Missing database value.')
    if table is None:
        raise ValueError('Missing table value.')
    for esedb_record in table.records:
        if parser_mediator.abort:
            break
        record_values = self._GetRecordValues(parser_mediator, table.name,
            esedb_record)
        event_data = MsieWebCacheContainersEventData()
        event_data.container_identifier = record_values.get('ContainerId', None
            )
        event_data.directory = record_values.get('Directory', None)
        event_data.name = record_values.get('Name', None)
        event_data.set_identifier = record_values.get('SetId', None)
        timestamp = record_values.get('LastScavengeTime', None)
        if timestamp:
            date_time = dfdatetime_filetime.Filetime(timestamp=timestamp)
            event = time_events.DateTimeValuesEvent(date_time,
                'Last Scavenge Time')
            parser_mediator.ProduceEventWithEventData(event, event_data)
        timestamp = record_values.get('LastAccessTime', None)
        if timestamp:
            date_time = dfdatetime_filetime.Filetime(timestamp=timestamp)
            event = time_events.DateTimeValuesEvent(date_time, definitions.
                TIME_DESCRIPTION_LAST_ACCESS)
            parser_mediator.ProduceEventWithEventData(event, event_data)
        container_identifier = record_values.get('ContainerId', None)
        container_name = record_values.get('Name', None)
        if not container_identifier or not container_name:
            continue
        table_name = 'Container_{0:d}'.format(container_identifier)
        esedb_table = database.get_table_by_name(table_name)
        if not esedb_table:
            parser_mediator.ProduceExtractionWarning('Missing table: {0:s}'
                .format(table_name))
            continue
        self._ParseContainerTable(parser_mediator, esedb_table, container_name)