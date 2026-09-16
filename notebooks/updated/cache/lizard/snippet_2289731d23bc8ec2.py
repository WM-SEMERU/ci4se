def read_machine_header(data):
    if isinstance(data, (bytes, bytearray)):
        stream = io.BytesIO(data)
    elif isinstance(data, io.BufferedReader):
        stream = data
    else:
        raise ValueError("data should be either bytearray or file 'rb' mode.")
    header = dict()
    header_type = stream.read(6)
    if header_type == b'#!\x00\x01@\x00':
        header['type'] = header_type[2:6]
        header['time'] = struct.unpack('>I', stream.read(4))[0]
        header['meta_type'] = struct.unpack('>I', stream.read(4))[0]
        header['meta_len'] = struct.unpack('>I', stream.read(4))[0]
        header['data_type'] = struct.unpack('>I', stream.read(4))[0]
        header['data_len'] = struct.unpack('>I', stream.read(4))[0]
        stream.read(4)
    elif header_type == b'#~DF02':
        header['type'] = header_type[2:6]
        header['meta_type'] = stream.read(2)
        header['meta_len'] = struct.unpack('>I', stream.read(4))[0]
        header['data_len'] = struct.unpack('>I', stream.read(4))[0]
        stream.read(4)
    else:
        raise NotImplementedError(
            'Parser for machine header %s not implemented' % header_type.
            decode())
    return header