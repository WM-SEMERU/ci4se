def GetMessages(self, formatter_mediator, event):
    if self.DATA_TYPE != event.data_type:
        raise errors.WrongFormatter('Unsupported data type: {0:s}.'.format(
            event.data_type))
    event_values = event.CopyToDict()
    event_type = event_values.get('event_type', None)
    if event_type is not None:
        event_values['event_type'] = self.GetEventTypeString(event_type)
    severity = event_values.get('severity', None)
    if severity is not None:
        event_values['severity'] = self.GetSeverityString(severity)
    source_name = event_values.get('source_name', None)
    message_identifier = event_values.get('message_identifier', None)
    strings = event_values.get('strings', [])
    if source_name and message_identifier:
        message_string = formatter_mediator.GetWindowsEventMessage(source_name,
            message_identifier)
        if message_string:
            try:
                event_values['message_string'] = message_string.format(*strings
                    )
            except IndexError:
                pass
    message_strings = []
    for string in strings:
        message_strings.append("'{0:s}'".format(string))
    message_string = ', '.join(message_strings)
    event_values['strings'] = '[{0:s}]'.format(message_string)
    return self._ConditionalFormatMessages(event_values)