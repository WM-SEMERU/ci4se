def seqToKV(seq, strict=False):

    def err(msg):
        formatted = 'seqToKV warning: %s: %r' % (msg, seq)
        if strict:
            raise KVFormError(formatted)
        else:
            logging.warn(formatted)
    lines = []
    for k, v in seq:
        if isinstance(k, types.StringType):
            k = k.decode('UTF8')
        elif not isinstance(k, types.UnicodeType):
            err('Converting key to string: %r' % k)
            k = str(k)
        if '\n' in k:
            raise KVFormError(
                'Invalid input for seqToKV: key contains newline: %r' % (k,))
        if ':' in k:
            raise KVFormError(
                'Invalid input for seqToKV: key contains colon: %r' % (k,))
        if k.strip() != k:
            err('Key has whitespace at beginning or end: %r' % (k,))
        if isinstance(v, types.StringType):
            v = v.decode('UTF8')
        elif not isinstance(v, types.UnicodeType):
            err('Converting value to string: %r' % (v,))
            v = str(v)
        if '\n' in v:
            raise KVFormError(
                'Invalid input for seqToKV: value contains newline: %r' % (v,))
        if v.strip() != v:
            err('Value has whitespace at beginning or end: %r' % (v,))
        lines.append(k + ':' + v + '\n')
    return ''.join(lines).encode('UTF8')