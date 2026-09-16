def _parse_user_id(stream, packet_type='user_id'):
    value = stream.read()
    to_hash = b'\xb4' + util.prefix_len('>L', value)
    return {'type': packet_type, 'value': value, '_to_hash': to_hash}