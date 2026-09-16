def _ConvertValueBinaryDataToFloatingPointValue(self, value):
    if not value:
        return None
    value_length = len(value)
    if value_length not in (4, 8):
        raise errors.ParseError('Unsupported value data size: {0:d}'.format
            (value_length))
    if value_length == 4:
        floating_point_map = self._GetDataTypeMap('float32le')
    elif value_length == 8:
        floating_point_map = self._GetDataTypeMap('float64le')
    try:
        return self._ReadStructureFromByteStream(value, 0, floating_point_map)
    except (ValueError, errors.ParseError) as exception:
        raise errors.ParseError(
            'Unable to parse floating-point value with error: {0!s}'.format
            (exception))