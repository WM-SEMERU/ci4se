def get_string(_bytearray, byte_index, max_size):
    size = _bytearray[byte_index + 1]
    if max_size < size:
        logger.error(
            'the string is to big for the size encountered in specification')
        logger.error('WRONG SIZED STRING ENCOUNTERED')
        size = max_size
    data = map(chr, _bytearray[byte_index + 2:byte_index + 2 + size])
    return ''.join(data)