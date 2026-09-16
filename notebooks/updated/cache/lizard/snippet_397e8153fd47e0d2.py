def load(fp, no_bytes=False, object_hook=None, object_pairs_hook=None,
    intern_object_keys=False):
    if object_pairs_hook is None and object_hook is None:
        object_hook = __object_hook_noop
    if not callable(fp.read):
        raise TypeError('fp.read not callable')
    fp_read = fp.read
    marker = fp_read(1)
    try:
        try:
            return __METHOD_MAP[marker](fp_read, marker)
        except KeyError:
            pass
        if marker == ARRAY_START:
            return __decode_array(fp_read, bool(no_bytes), object_hook,
                object_pairs_hook, intern_object_keys)
        elif marker == OBJECT_START:
            return __decode_object(fp_read, bool(no_bytes), object_hook,
                object_pairs_hook, intern_object_keys)
        else:
            raise DecoderException('Invalid marker')
    except DecoderException as ex:
        raise_from(DecoderException(ex.args[0], fp), ex)