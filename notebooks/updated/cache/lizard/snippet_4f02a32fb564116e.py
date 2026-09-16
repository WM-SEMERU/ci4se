def validate_stream(stream):
    if not STREAM_REGEX.match(stream) or len(stream) > MAX_STREAM_LENGTH:
        raise InvalidStreamName(stream)