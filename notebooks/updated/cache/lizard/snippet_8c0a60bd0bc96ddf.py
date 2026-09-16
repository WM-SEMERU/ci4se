def iter_vcf_chunks(input, fields=None, exclude_fields=None, types=None,
    numbers=None, alt_number=DEFAULT_ALT_NUMBER, fills=None, region=None,
    tabix='tabix', samples=None, transformers=None, buffer_size=
    DEFAULT_BUFFER_SIZE, chunk_length=DEFAULT_CHUNK_LENGTH):
    kwds = dict(fields=fields, exclude_fields=exclude_fields, types=types,
        numbers=numbers, alt_number=alt_number, chunk_length=chunk_length,
        fills=fills, samples=samples, region=region)
    stream = _setup_input_stream(input=input, region=region, tabix=tabix,
        buffer_size=buffer_size)
    fields, samples, headers, it = _iter_vcf_stream(stream, **kwds)
    if transformers is not None:
        if not isinstance(transformers, (list, tuple)):
            transformers = [transformers]
        for trans in transformers:
            fields = trans.transform_fields(fields)
        it = _chunk_iter_transform(it, transformers)
    return fields, samples, headers, it