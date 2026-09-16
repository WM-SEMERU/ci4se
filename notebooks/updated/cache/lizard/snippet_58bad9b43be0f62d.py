def PackTag(field_number, wire_type):
    if not 0 <= wire_type <= _WIRETYPE_MAX:
        raise message.EncodeError('Unknown wire type: %d' % wire_type)
    return field_number << TAG_TYPE_BITS | wire_type