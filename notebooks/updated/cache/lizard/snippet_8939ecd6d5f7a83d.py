def _ReadCharacterDataTypeDefinition(self, definitions_registry,
    definition_values, definition_name, is_member=False):
    return self._ReadFixedSizeDataTypeDefinition(definitions_registry,
        definition_values, data_types.CharacterDefinition, definition_name,
        self._SUPPORTED_ATTRIBUTES_FIXED_SIZE_DATA_TYPE, is_member=
        is_member, supported_size_values=(1, 2, 4))