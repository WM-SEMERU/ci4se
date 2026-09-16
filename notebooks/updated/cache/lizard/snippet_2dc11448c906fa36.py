def _ParseFValue(self, registry_key):
    registry_value = registry_key.GetValueByName('F')
    if not registry_value:
        raise errors.ParseError(
            'missing value: "F" in Windows Registry key: {0:s}.'.format(
            registry_key.name))
    f_value_map = self._GetDataTypeMap('f_value')
    try:
        return self._ReadStructureFromByteStream(registry_value.data, 0,
            f_value_map)
    except (ValueError, errors.ParseError) as exception:
        raise errors.ParseError(exception)