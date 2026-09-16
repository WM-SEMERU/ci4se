def as_srec(self, number_of_data_bytes=32, address_length_bits=32):
    header = []
    if self._header is not None:
        record = pack_srec('0', 0, len(self._header), self._header)
        header.append(record)
    type_ = str(address_length_bits // 8 - 1)
    if type_ not in '123':
        raise Error('expected data record type 1..3, but got {}'.format(type_))
    data = [pack_srec(type_, address, len(data), data) for address, data in
        self._segments.chunks(number_of_data_bytes)]
    number_of_records = len(data)
    if number_of_records <= 65535:
        footer = [pack_srec('5', number_of_records, 0, None)]
    elif number_of_records <= 16777215:
        footer = [pack_srec('6', number_of_records, 0, None)]
    else:
        raise Error('too many records {}'.format(number_of_records))
    if self.execution_start_address is not None:
        if type_ == '1':
            record = pack_srec('9', self.execution_start_address, 0, None)
        elif type_ == '2':
            record = pack_srec('8', self.execution_start_address, 0, None)
        else:
            record = pack_srec('7', self.execution_start_address, 0, None)
        footer.append(record)
    return '\n'.join(header + data + footer) + '\n'