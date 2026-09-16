def _ReadString(self, file_object, file_offset, data_type_map, description):
    element_data_size = (data_type_map._element_data_type_definition.
        GetByteSize())
    elements_terminator = (data_type_map._data_type_definition.
        elements_terminator)
    byte_stream = []
    element_data = file_object.read(element_data_size)
    byte_stream.append(element_data)
    while element_data and element_data != elements_terminator:
        element_data = file_object.read(element_data_size)
        byte_stream.append(element_data)
    byte_stream = b''.join(byte_stream)
    return self._ReadStructureFromByteStream(byte_stream, file_offset,
        data_type_map, description)