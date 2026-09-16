def write_key_val(stream, key, val, linesep=os.linesep):
    key = key.encode('utf-8') or ''
    val = val.encode('utf-8') or ''
    linesep = linesep.encode('utf-8')
    if not 0 < len(key) < 69:
        raise ManifestKeyException('bad key length', key)
    if len(key) + len(val) > 68:
        kvbuffer = BytesIO(b': '.join((key, val)))
        stream.write(kvbuffer.read(70))
        part = kvbuffer.read(69)
        while part:
            stream.write(linesep + b' ')
            stream.write(part)
            part = kvbuffer.read(69)
        kvbuffer.close()
    else:
        stream.write(key)
        stream.write(b': ')
        stream.write(val)
    stream.write(linesep)