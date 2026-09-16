def _ReadSequenceDataTypeDefinition(self, definitions_registry,
    definition_values, definition_name, is_member=False):
    if is_member:
        supported_definition_values = (self.
            _SUPPORTED_DEFINITION_VALUES_ELEMENTS_MEMBER_DATA_TYPE)
    else:
        supported_definition_values = (self.
            _SUPPORTED_DEFINITION_VALUES_ELEMENTS_DATA_TYPE)
    return self._ReadElementSequenceDataTypeDefinition(definitions_registry,
        definition_values, data_types.SequenceDefinition, definition_name,
        supported_definition_values)