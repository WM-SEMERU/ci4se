def make_op_return_script(data, format='bin'):
    if format == 'hex':
        assert is_hex(data)
        hex_data = data
    elif format == 'bin':
        hex_data = hexlify(data)
    else:
        raise Exception("Format must be either 'hex' or 'bin'")
    num_bytes = count_bytes(hex_data)
    if num_bytes > MAX_BYTES_AFTER_OP_RETURN:
        raise Exception('Data is %i bytes - must not exceed 40.' % num_bytes)
    script_string = 'OP_RETURN %s' % hex_data
    return script_to_hex(script_string)