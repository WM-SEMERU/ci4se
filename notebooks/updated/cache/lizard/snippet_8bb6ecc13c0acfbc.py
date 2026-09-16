def ParseSearchRow(self, parser_mediator, query, row, **unused_kwargs):
    query_hash = hash(query)
    event_data = TwitterAndroidSearchEventData()
    event_data.query = query
    event_data.name = self._GetRowValue(query_hash, row, 'name')
    event_data.search_query = self._GetRowValue(query_hash, row, 'query')
    timestamp = self._GetRowValue(query_hash, row, 'time')
    if timestamp:
        date_time = dfdatetime_java_time.JavaTime(timestamp=timestamp)
        event = time_events.DateTimeValuesEvent(date_time, definitions.
            TIME_DESCRIPTION_CREATION)
        parser_mediator.ProduceEventWithEventData(event, event_data)