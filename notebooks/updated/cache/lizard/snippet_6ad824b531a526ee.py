def GetMessages(self, formatter_mediator, event):
    if self.DATA_TYPE != event.data_type:
        raise errors.WrongFormatter('Unsupported data type: {0:s}.'.format(
            event.data_type))
    event_values = event.CopyToDict()
    security = event_values.get('security', None)
    if security:
        security_flags = []
        for flag, description in iter(self._SECURITY_VALUES.items()):
            if security & flag:
                security_flags.append(description)
        security_string = '0x{0:08x}: {1:s}'.format(security, ','.join(
            security_flags))
        event_values['security'] = security_string
    for key, value in iter(event_values.items()):
        if isinstance(value, py2to3.BYTES_TYPE):
            event_values[key] = repr(value)
    return self._ConditionalFormatMessages(event_values)