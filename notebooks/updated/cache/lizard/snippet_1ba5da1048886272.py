def _safe_match_string(value):
    if not isinstance(value, six.string_types):
        if isinstance(value, bytes):
            value = value.decode('utf-8')
        else:
            raise GraphQLInvalidArgumentError(
                'Attempting to convert a non-string into a string: {}'.
                format(value))
    return json.dumps(value)