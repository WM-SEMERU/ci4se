def hex_timestamp_to_datetime(hex_timestamp):
    if not hex_timestamp.startswith('0x'):
        hex_timestamp = '0x{0}'.format(hex_timestamp)
    return datetime.fromtimestamp(int(hex_timestamp, 16))