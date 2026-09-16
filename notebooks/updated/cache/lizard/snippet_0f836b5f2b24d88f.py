def FromBinary(cls, record_data, record_count=1):
    _cmd, address, _resp_length, payload = cls._parse_rpc_info(record_data)
    try:
        value, encoded_stream = struct.unpack('<LH', payload)
        stream = DataStream.FromEncoded(encoded_stream)
    except ValueError:
        raise ArgumentError('Could not parse set_constant payload', payload
            =payload)
    return SetConstantRecord(stream, value, address=address)