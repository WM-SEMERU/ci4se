def GetDataAsObject(self):
    if self._pyregf_value.type in self._STRING_VALUE_TYPES:
        try:
            return self._pyregf_value.get_data_as_string()
        except IOError as exception:
            raise errors.WinRegistryValueError(
                'Unable to read data from value: {0:s} with error: {1!s}'.
                format(self._pyregf_value.name, exception))
    if self._pyregf_value.type in self._INTEGER_VALUE_TYPES:
        try:
            return self._pyregf_value.get_data_as_integer()
        except (IOError, OverflowError) as exception:
            raise errors.WinRegistryValueError(
                'Unable to read data from value: {0:s} with error: {1!s}'.
                format(self._pyregf_value.name, exception))
    try:
        value_data = self._pyregf_value.data
    except IOError as exception:
        raise errors.WinRegistryValueError(
            'Unable to read data from value: {0:s} with error: {1!s}'.
            format(self._pyregf_value.name, exception))
    if self._pyregf_value.type == definitions.REG_MULTI_SZ:
        if value_data is None:
            return []
        try:
            utf16_string = value_data.decode('utf-16-le')
            return list(filter(None, utf16_string.split('\x00')))
        except UnicodeError as exception:
            raise errors.WinRegistryValueError(
                'Unable to read data from value: {0:s} with error: {1!s}'.
                format(self._pyregf_value.name, exception))
    return value_data