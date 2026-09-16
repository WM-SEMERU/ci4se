def loads(cls, data):
    rep = cbor.loads(data)
    if not isinstance(rep, Sequence):
        raise SerializationError('expected a CBOR list')
    if len(rep) != 2:
        raise SerializationError('expected a CBOR list of 2 items')
    metadata = rep[0]
    if 'v' not in metadata:
        raise SerializationError('no version in CBOR metadata')
    if metadata['v'] != 'fc01':
        raise SerializationError('invalid CBOR version {!r} (expected "fc01")'
            .format(metadata['v']))
    read_only = metadata.get('ro', False)
    contents = rep[1]
    return cls.from_dict(contents, read_only=read_only)