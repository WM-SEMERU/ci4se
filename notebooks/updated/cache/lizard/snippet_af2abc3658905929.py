def encode(encoding, data):
    data = ensure_bytes(data, 'utf8')
    try:
        return ENCODINGS_LOOKUP[encoding].code + ENCODINGS_LOOKUP[encoding
            ].converter.encode(data)
    except KeyError:
        raise ValueError('Encoding {} not supported.'.format(encoding))