def _read_frame(self, length):
    response = self._read_data(length + 8)
    logger.debug('Read frame: 0x{0}'.format(binascii.hexlify(response)))
    if response[0] != 1:
        raise RuntimeError('Response frame does not start with 0x01!')
    offset = 1
    while response[offset] == 0:
        offset += 1
        if offset >= len(response):
            raise RuntimeError(
                'Response frame preamble does not contain 0x00FF!')
    if response[offset] != 255:
        raise RuntimeError('Response frame preamble does not contain 0x00FF!')
    offset += 1
    if offset >= len(response):
        raise RuntimeError('Response contains no data!')
    frame_len = response[offset]
    if frame_len + response[offset + 1] & 255 != 0:
        raise RuntimeError('Response length checksum did not match length!')
    checksum = reduce(self._uint8_add, response[offset + 2:offset + 2 +
        frame_len + 1], 0)
    if checksum != 0:
        raise RuntimeError('Response checksum did not match expected value!')
    return response[offset + 2:offset + 2 + frame_len]