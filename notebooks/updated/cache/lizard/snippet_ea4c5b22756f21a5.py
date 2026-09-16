def _VarintDecoder(mask):

    def DecodeVarint(buffer, pos):
        result = 0
        shift = 0
        while 1:
            if pos > len(buffer) - 1:
                raise NotEnoughDataException('Not enough data to decode varint'
                    )
            b = buffer[pos]
            result |= (b & 127) << shift
            pos += 1
            if not b & 128:
                result &= mask
                return result, pos
            shift += 7
            if shift >= 64:
                raise _DecodeError('Too many bytes when decoding varint.')
    return DecodeVarint