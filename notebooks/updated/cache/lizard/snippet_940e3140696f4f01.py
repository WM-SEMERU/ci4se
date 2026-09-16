def generateAcceptHeader(*elements):
    parts = []
    for element in elements:
        if type(element) is str:
            qs = '1.0'
            mtype = element
        else:
            mtype, q = element
            q = float(q)
            if q > 1 or q <= 0:
                raise ValueError('Invalid preference factor: %r' % q)
            qs = '%0.1f' % (q,)
        parts.append((qs, mtype))
    parts.sort()
    chunks = []
    for q, mtype in parts:
        if q == '1.0':
            chunks.append(mtype)
        else:
            chunks.append('%s; q=%s' % (mtype, q))
    return ', '.join(chunks)