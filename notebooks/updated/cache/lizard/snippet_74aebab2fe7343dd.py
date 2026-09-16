def decode_dict(value_fields, client):
    return {key: decode_value(value, client) for key, value in six.
        iteritems(value_fields)}