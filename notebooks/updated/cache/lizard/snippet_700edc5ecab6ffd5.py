def get_crc(msg):
    register = 65535
    for byte_ in msg:
        try:
            val = struct.unpack('<B', byte_)[0]
        except TypeError:
            val = byte_
        register = register >> 8 ^ look_up_table[(register ^ val) & 255]
    return struct.pack('<H', register)