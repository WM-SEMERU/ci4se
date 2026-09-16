def GetMessage(self, log_source, lcid, message_identifier):
    event_log_provider_key = self._GetEventLogProviderKey(log_source)
    if not event_log_provider_key:
        return None
    generator = self._GetMessageFileKeys(event_log_provider_key)
    if not generator:
        return None
    message_string = None
    for message_file_key in generator:
        message_string = self._GetMessage(message_file_key, lcid,
            message_identifier)
        if message_string:
            break
    if self._string_format == 'wrc':
        message_string = self._ReformatMessageString(message_string)
    return message_string