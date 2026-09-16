def ParsePartitionsTable(self, parser_mediator, database=None, table=None,
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
        event_data = MsieWebCachePartitionsEventData()
        event_data.directory = record_values.get('Directory', None)
        event_data.partition_identifier = record_values.get('PartitionId', None
            )
        event_data.partition_type = record_values.get('PartitionType', None)
        event_data.table_identifier = record_values.get('TableId', None)
        timestamp = record_values.get('LastScavengeTime', None)
        if timestamp:
            date_time = dfdatetime_filetime.Filetime(timestamp=timestamp)
            event = time_events.DateTimeValuesEvent(date_time,
                'Last Scavenge Time')
            parser_mediator.ProduceEventWithEventData(event, event_data)