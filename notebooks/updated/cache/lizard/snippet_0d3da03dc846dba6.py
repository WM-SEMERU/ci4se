def _ReadStructureDataTypeDefinition(self, definitions_registry,
    definition_values, definition_name, is_member=False):
    if is_member:
        error_message = 'data type not supported as member'
        raise errors.DefinitionReaderError(definition_name, error_message)
    return self._ReadDataTypeDefinitionWithMembers(definitions_registry,
        definition_values, data_types.StructureDefinition, definition_name,
        supports_conditions=True)