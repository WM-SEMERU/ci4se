def attributesToBinary(cls, attributes):
    chunks = [(int(k), v) for k, v in iteritems(attributes) if cls.
        _isValidChunkName(k)]
    chunks.sort()
    numChunks = int(attributes['numChunks'])
    if numChunks:
        serializedJob = b''.join(v for k, v in chunks)
        compressed = base64.b64decode(serializedJob)
        if compressed[0] == b'C'[0]:
            binary = bz2.decompress(compressed[1:])
        elif compressed[0] == b'U'[0]:
            binary = compressed[1:]
        else:
            raise RuntimeError('Unexpected prefix {}'.format(compressed[0]))
    else:
        binary = None
    return binary, numChunks