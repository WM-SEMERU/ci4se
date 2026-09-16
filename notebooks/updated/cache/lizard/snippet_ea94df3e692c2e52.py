def FromBinary(cls, record_data, record_count=1):
    rpcs = SendErrorCheckingRPCRecord.parse_multiple_rpcs(record_data)
    start_rpc = rpcs[0]
    push_rpcs = rpcs[1:-1]
    try:
        config_id, raw_target = struct.unpack('<H8s', start_rpc.payload)
        target = SlotIdentifier.FromEncoded(raw_target)
    except ValueError:
        raise ArgumentError('Could not parse payload on begin config rpc',
            payload=start_rpc.payload)
    payload = bytearray()
    for rpc in push_rpcs:
        payload += rpc.payload
    return SetConfigRecord(target, config_id, payload)