def MapByteStream(self, byte_stream, byte_offset=0, context=None, **
    unused_kwargs):
    data_type_size = self._data_type_definition.GetByteSize()
    self._CheckByteStreamSize(byte_stream, byte_offset, data_type_size)
    try:
        if self._byte_order == definitions.BYTE_ORDER_BIG_ENDIAN:
            mapped_value = uuid.UUID(bytes=byte_stream[byte_offset:
                byte_offset + 16])
        elif self._byte_order == definitions.BYTE_ORDER_LITTLE_ENDIAN:
            mapped_value = uuid.UUID(bytes_le=byte_stream[byte_offset:
                byte_offset + 16])
    except Exception as exception:
        error_string = (
            'Unable to read: {0:s} from byte stream at offset: {1:d} with error: {2!s}'
            .format(self._data_type_definition.name, byte_offset, exception))
        raise errors.MappingError(error_string)
    if context:
        context.byte_size = data_type_size
    return mapped_value