def ParseCloudEntryRow(self, parser_mediator, query, row, cache=None,
    database=None, **unused_kwargs):
    query_hash = hash(query)
    parent_resource_id = self._GetRowValue(query_hash, row,
        'parent_resource_id')
    filename = self._GetRowValue(query_hash, row, 'filename')
    cloud_path = self.GetCloudPath(parent_resource_id, cache, database)
    cloud_filename = '{0:s}{1:s}'.format(cloud_path, filename)
    event_data = GoogleDriveSnapshotCloudEntryEventData()
    event_data.document_type = self._GetRowValue(query_hash, row, 'doc_type')
    event_data.path = cloud_filename
    event_data.query = query
    event_data.shared = bool(self._GetRowValue(query_hash, row, 'shared'))
    event_data.size = self._GetRowValue(query_hash, row, 'size')
    event_data.url = self._GetRowValue(query_hash, row, 'url')
    timestamp = self._GetRowValue(query_hash, row, 'modified')
    date_time = dfdatetime_posix_time.PosixTime(timestamp=timestamp)
    event = time_events.DateTimeValuesEvent(date_time, definitions.
        TIME_DESCRIPTION_MODIFICATION)
    parser_mediator.ProduceEventWithEventData(event, event_data)
    timestamp = self._GetRowValue(query_hash, row, 'created')
    if timestamp:
        date_time = dfdatetime_posix_time.PosixTime(timestamp=timestamp)
        event = time_events.DateTimeValuesEvent(date_time, definitions.
            TIME_DESCRIPTION_CREATION)
        parser_mediator.ProduceEventWithEventData(event, event_data)