def _get_next_chunk(fp, previously_read_position, chunk_size):
    seek_position, read_size = _get_what_to_read_next(fp,
        previously_read_position, chunk_size)
    fp.seek(seek_position)
    read_content = fp.read(read_size)
    read_position = seek_position
    return read_content, read_position