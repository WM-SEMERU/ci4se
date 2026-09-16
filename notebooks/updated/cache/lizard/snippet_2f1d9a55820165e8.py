def from_serializable(cls, obj):
    schema_version = '2.0.0'
    if obj['version']['sampleset_schema'] == '1.0.0':
        import warnings
        msg = (
            'sampleset is serialized with a deprecated format and will no longer work in dimod 0.9.0.'
            )
        warnings.warn(msg)
        from dimod.serialization.json import sampleset_decode_hook
        return sampleset_decode_hook(obj, cls=cls)
    elif obj['version']['sampleset_schema'] != schema_version:
        raise ValueError('cannot load legacy serialization formats')
    vartype = Vartype[obj['variable_type']]
    if obj['use_bytes']:
        record = obj['record']
    else:
        record = {name: base64.b64decode(vector) for name, vector in obj[
            'record'].items()}
    vectors = {name: bytes2array(vector) for name, vector in record.items()}
    shape = obj['sample_shape']
    dtype = obj['sample_dtype']
    sample = np.unpackbits(vectors.pop('sample'))[:shape[0] * shape[1]].astype(
        dtype).reshape(shape)
    if vartype is Vartype.SPIN:
        sample = np.asarray(2 * sample - 1, dtype=dtype)
    variables = [(tuple(v) if isinstance(v, list) else v) for v in obj[
        'variable_labels']]
    info = obj['info']
    return cls.from_samples((sample, variables), vartype, info=info, **vectors)