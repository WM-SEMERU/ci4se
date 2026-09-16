def _is_binary_stl(data):
    is_bin = False
    start_byte = 0
    end_byte = 80
    _ = data[start_byte:end_byte]
    start_byte = end_byte
    end_byte += 4
    facet_count = struct.unpack('I', data[start_byte:end_byte])[0]
    if facet_count > 0:
        is_bin = True
    return is_bin