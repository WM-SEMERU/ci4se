def _get_timestamp(data, position, dummy0, dummy1, dummy2):
    end = position + 8
    inc, timestamp = _UNPACK_TIMESTAMP(data[position:end])
    return Timestamp(timestamp, inc), end