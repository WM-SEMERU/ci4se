def _from_json_array_nested(cls, response_raw):
    json = response_raw.body_bytes.decode()
    obj = converter.json_to_class(dict, json)
    value = converter.deserialize(cls, obj[cls._FIELD_RESPONSE])
    return client.BunqResponse(value, response_raw.headers)