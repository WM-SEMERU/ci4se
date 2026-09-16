def get_file_hash(file, seed, bufsz=DEFAULT_BUFFER_SIZE):
    h = hmac.new(seed, None, hashlib.sha256)
    while True:
        buffer = file.read(bufsz)
        h.update(buffer)
        if len(buffer) != bufsz:
            break
    return h.digest()