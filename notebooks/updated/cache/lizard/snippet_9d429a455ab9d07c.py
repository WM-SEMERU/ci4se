def _get_boolean(data, position, dummy0, dummy1, dummy2):
    end = position + 1
    boolean_byte = data[position:end]
    if boolean_byte == b'\x00':
        return False, end
    elif boolean_byte == b'\x01':
        return True, end
    raise InvalidBSON('invalid boolean value: %r' % boolean_byte)