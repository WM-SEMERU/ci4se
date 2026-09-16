def binary_tlv_to_python(binary_string, result=None):
    result = {} if result is None else result
    if not binary_string:
        return result
    byte = binary_string[0]
    kind = byte & type_mask
    id_length = get_id_length(byte)
    payload_length = get_value_length(byte)
    offset = 1
    item_id = str(combine_bytes(binary_string[offset:offset + id_length]))
    offset += id_length
    value_length = payload_length
    if byte & length_type_mask != LengthTypes.SET_BYTE:
        value_length = combine_bytes(binary_string[offset:offset +
            payload_length])
        offset += payload_length
    if kind == Types.MULTI:
        binary_tlv_to_python(binary_string[offset:offset + value_length],
            result.setdefault(item_id, {}))
    else:
        value_binary = binary_string[offset:offset + value_length]
        result[item_id] = combine_bytes(value_binary) if not all(value_binary
            ) else value_binary.decode('utf8')
    offset += value_length
    binary_tlv_to_python(binary_string[offset:], result)
    return result