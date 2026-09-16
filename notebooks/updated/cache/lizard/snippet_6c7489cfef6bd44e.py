def convert_id36_to_numeric_id(id36):
    if not isinstance(id36, six.string_types) or id36.count('_') > 0:
        raise ValueError(
            'must supply base36 string, not fullname (e.g. use xxxxx, not t3_xxxxx)'
            )
    return int(id36, 36)