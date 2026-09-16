def _ParseIndexTable(self, file_object):
    cache_address_map = self._GetDataTypeMap('uint32le')
    file_offset = file_object.get_offset()
    cache_address_data = file_object.read(4)
    while len(cache_address_data) == 4:
        try:
            value = self._ReadStructureFromByteStream(cache_address_data,
                file_offset, cache_address_map)
        except (ValueError, errors.ParseError) as exception:
            raise errors.ParseError(
                'Unable to map cache address at offset: 0x{0:08x} with error: {1!s}'
                .format(file_offset, exception))
        if value:
            cache_address = CacheAddress(value)
            self.index_table.append(cache_address)
        file_offset += 4
        cache_address_data = file_object.read(4)