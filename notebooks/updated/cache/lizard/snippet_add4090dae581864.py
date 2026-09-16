def add_ihex(self, records, overwrite=False):
    extended_segment_address = 0
    extended_linear_address = 0
    for record in StringIO(records):
        type_, address, size, data = unpack_ihex(record.strip())
        if type_ == IHEX_DATA:
            address = (address + extended_segment_address +
                extended_linear_address)
            address *= self.word_size_bytes
            self._segments.add(_Segment(address, address + size, bytearray(
                data), self.word_size_bytes), overwrite)
        elif type_ == IHEX_END_OF_FILE:
            pass
        elif type_ == IHEX_EXTENDED_SEGMENT_ADDRESS:
            extended_segment_address = int(binascii.hexlify(data), 16)
            extended_segment_address *= 16
        elif type_ == IHEX_EXTENDED_LINEAR_ADDRESS:
            extended_linear_address = int(binascii.hexlify(data), 16)
            extended_linear_address <<= 16
        elif type_ in [IHEX_START_SEGMENT_ADDRESS, IHEX_START_LINEAR_ADDRESS]:
            self.execution_start_address = int(binascii.hexlify(data), 16)
        else:
            raise Error('expected type 1..5 in record {}, but got {}'.
                format(record, type_))