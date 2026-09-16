def from_json(cls, stream, json_data):
    type_converter = _get_decoder_method(stream.get_data_type())
    data = type_converter(json_data.get('data'))
    return cls(stream_id=stream.get_stream_id(), data_type=stream.
        get_data_type(), units=stream.get_units(), data=data, description=
        json_data.get('description'), timestamp=json_data.get(
        'timestampISO'), server_timestamp=json_data.get(
        'serverTimestampISO'), quality=json_data.get('quality'), location=
        json_data.get('location'), dp_id=json_data.get('id'))