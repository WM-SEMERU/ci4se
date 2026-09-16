def MapByteStream(self, byte_stream, **unused_kwargs):
    raise errors.MappingError('Unable to map {0:s} data type to byte stream'
        .format(self._data_type_definition.TYPE_INDICATOR))