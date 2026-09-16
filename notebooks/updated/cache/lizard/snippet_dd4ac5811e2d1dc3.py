def GetMessages(self, formatter_mediator, event):
    if self.DATA_TYPE != event.data_type:
        raise errors.WrongFormatter('Unsupported data type: {0:s}.'.format(
            event.data_type))
    event_values = event.CopyToDict()
    attribute_type = event_values.get('attribute_type', 0)
    event_values['attribute_name'] = self._ATTRIBUTE_NAMES.get(attribute_type,
        'UNKNOWN')
    file_reference = event_values.get('file_reference', None)
    if file_reference:
        event_values['file_reference'] = '{0:d}-{1:d}'.format(
            file_reference & 281474976710655, file_reference >> 48)
    parent_file_reference = event_values.get('parent_file_reference', None)
    if parent_file_reference:
        event_values['parent_file_reference'] = '{0:d}-{1:d}'.format(
            parent_file_reference & 281474976710655, parent_file_reference >>
            48)
    if not event_values.get('is_allocated', False):
        event_values['unallocated'] = 'unallocated'
    return self._ConditionalFormatMessages(event_values)