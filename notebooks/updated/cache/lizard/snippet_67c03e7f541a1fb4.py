def _ParseTokenType(self, file_object, file_offset):
    token_type_map = self._GetDataTypeMap('uint8')
    token_type, _ = self._ReadStructureFromFileObject(file_object,
        file_offset, token_type_map)
    return token_type