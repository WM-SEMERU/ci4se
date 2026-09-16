def _ReadData(self, file_object, file_offset, data_size):
    if not file_object:
        raise ValueError('Missing file-like object.')
    file_object.seek(file_offset, os.SEEK_SET)
    read_error = ''
    try:
        data = file_object.read(data_size)
        if len(data) != data_size:
            read_error = 'missing data'
    except IOError as exception:
        read_error = '{0!s}'.format(exception)
    if read_error:
        raise errors.ParseError(
            'Unable to read data at offset: 0x{0:08x} with error: {1:s}'.
            format(file_offset, read_error))
    return data