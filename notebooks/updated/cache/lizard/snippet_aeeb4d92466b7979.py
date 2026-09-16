def _pfp__build(self, stream=None, save_offset=False):
    max_size = -1
    if stream is None:
        core_stream = six.BytesIO()
        new_stream = bitwrap.BitwrappedStream(core_stream)
    else:
        new_stream = stream
    for child in self._pfp__children:
        curr_pos = new_stream.tell()
        child._pfp__build(new_stream, save_offset)
        size = new_stream.tell() - curr_pos
        new_stream.seek(-size, 1)
        if size > max_size:
            max_size = size
    new_stream.seek(max_size, 1)
    if stream is None:
        return core_stream.getvalue()
    else:
        return max_size