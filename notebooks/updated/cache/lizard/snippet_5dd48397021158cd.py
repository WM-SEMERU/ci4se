def FromString(cls, string_rep):
    rep = str(string_rep)
    parts = rep.split()
    if len(parts) > 3:
        raise ArgumentError(
            'Too many whitespace separated parts of stream designator',
            input_string=string_rep)
    elif len(parts) == 3 and parts[0] != 'system':
        raise ArgumentError(
            'Too many whitespace separated parts of stream designator',
            input_string=string_rep)
    elif len(parts) < 2:
        raise ArgumentError('Too few components in stream designator',
            input_string=string_rep)
    if len(parts) == 3:
        system = True
        stream_type = parts[1]
        stream_id = parts[2]
    else:
        system = False
        stream_type = parts[0]
        stream_id = parts[1]
    try:
        stream_id = int(stream_id, 0)
    except ValueError as exc:
        raise ArgumentError('Could not convert stream id to integer',
            error_string=str(exc), stream_id=stream_id)
    try:
        stream_type = cls.StringToType[stream_type]
    except KeyError:
        raise ArgumentError('Invalid stream type given', stream_type=
            stream_type, known_types=cls.StringToType.keys())
    return DataStream(stream_type, stream_id, system)