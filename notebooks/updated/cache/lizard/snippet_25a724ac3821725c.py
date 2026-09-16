def open(filepath, mode='rb', buffcompress=None):
    root, ext = splitext(filepath.replace('.gz', ''))
    ext = ext[1:]
    if filepath.endswith('.gz'):
        compress = buffcompress
        if compress is None:
            compress = 9
        handle = gzip.open(filepath, mode, compress)
    else:
        buffer = buffcompress
        if buffer is None:
            buffer = -1
        handle = builtins.open(filepath, mode, buffer)
    return handle, ext