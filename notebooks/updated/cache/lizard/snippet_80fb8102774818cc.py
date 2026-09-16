def _get_sd(file_descr):
    for stream_descr in NonBlockingStreamReader._streams:
        if file_descr == stream_descr.stream.fileno():
            return stream_descr
    return None