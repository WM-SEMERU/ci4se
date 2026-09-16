def copyfileobj(src, dst, length=None, exception=OSError):
    if length == 0:
        return
    if length is None:
        shutil.copyfileobj(src, dst)
        return
    blocks, remainder = divmod(length, BUFSIZE)
    for _ in range(blocks):
        buf = src.read(BUFSIZE)
        if len(buf) < BUFSIZE:
            raise exception('unexpected end of data')
        dst.write(buf)
    if remainder != 0:
        buf = src.read(remainder)
        if len(buf) < remainder:
            raise exception('unexpected end of data')
        dst.write(buf)
    return