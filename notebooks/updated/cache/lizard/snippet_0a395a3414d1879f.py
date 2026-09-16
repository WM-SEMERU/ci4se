def replace_with_text_stream(stream_name):
    new_stream = TEXT_STREAMS.get(stream_name)
    if new_stream is not None:
        new_stream = new_stream()
        setattr(sys, stream_name, new_stream)
    return None