def recommended_overlap(name, nfft=None):
    try:
        name = canonical_name(name)
    except KeyError as exc:
        raise ValueError(str(exc))
    try:
        rov = ROV[name]
    except KeyError:
        raise ValueError('no recommended overlap for %r window' % name)
    if nfft:
        return int(ceil(nfft * rov))
    return rov