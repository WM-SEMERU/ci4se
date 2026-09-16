def _wrap_callback_parse_stream_data(subscription, on_data, message):
    if (message.type == message.DATA and message.data.type == yamcs_pb2.
        STREAM_DATA):
        stream_data = getattr(message.data, 'streamData')
        on_data(StreamData(stream_data))