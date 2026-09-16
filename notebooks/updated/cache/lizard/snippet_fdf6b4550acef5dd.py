def ParseMessage(self, parser_mediator, key, date_time, tokens):
    if key != 'task_run':
        raise ValueError('Unknown grammar key: {0:s}'.format(key))
    event_data = CronTaskRunEventData()
    event_data.body = tokens.get('body', None)
    event_data.command = tokens.get('command', None)
    event_data.hostname = tokens.get('hostname', None)
    event_data.offset = 0
    event_data.pid = tokens.get('pid', None)
    event_data.reporter = tokens.get('reporter', None)
    event_data.severity = tokens.get('severity', None)
    event_data.username = tokens.get('username', None)
    event = time_events.DateTimeValuesEvent(date_time, definitions.
        TIME_DESCRIPTION_WRITTEN)
    parser_mediator.ProduceEventWithEventData(event, event_data)