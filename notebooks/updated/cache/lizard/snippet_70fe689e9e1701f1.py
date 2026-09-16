def blank_stamp(name=None, backdate=None, unique=None, keep_subdivisions=
    False, quick_print=None, un=None, ks=False, qp=None):
    t = timer()
    if f.t.stopped:
        raise StoppedError('Cannot blank_stamp stopped timer.')
    keep_subdivisions = keep_subdivisions or ks
    times_priv.assign_subdivisions(UNASGN, keep_subdivisions)
    f.t.last_t = timer()
    f.t.self_cut += f.t.last_t - t
    return t