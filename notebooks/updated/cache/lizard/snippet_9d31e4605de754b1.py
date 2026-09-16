def try_encode(field_encoders, entity_dict):
    result = ''
    for field_encoder in field_encoders:
        try:
            result += field_encoder.encode(entity_dict)
        except KeyError as e:
            return False
    return result