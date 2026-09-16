def escape(data):
    escaped_data = b''
    for byte in data:
        if intToByte(byteToInt(byte)) in APIFrame.ESCAPE_BYTES:
            escaped_data += APIFrame.ESCAPE_BYTE
            escaped_data += intToByte(32 ^ byteToInt(byte))
        else:
            escaped_data += intToByte(byteToInt(byte))
    return escaped_data