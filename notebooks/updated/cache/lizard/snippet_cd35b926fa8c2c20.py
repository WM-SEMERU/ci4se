def event_id(name, encode_types):
    event_types = [_canonical_type(type_) for type_ in encode_types]
    event_signature = '{event_name}({canonical_types})'.format(event_name=
        name, canonical_types=','.join(event_types))
    return big_endian_to_int(utils.sha3(event_signature))