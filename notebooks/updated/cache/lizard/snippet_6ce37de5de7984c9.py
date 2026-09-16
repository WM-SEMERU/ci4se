def _file_iter_range(fp, offset, bytes, maxread=1024 * 1024):
    fp.seek(offset)
    while bytes > 0:
        part = fp.read(min(bytes, maxread))
        if not part:
            break
        bytes -= len(part)
        yield part