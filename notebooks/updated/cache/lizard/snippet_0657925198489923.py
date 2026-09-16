def duration_bool(b, rule, samplerate=None):
    if rule is None:
        return b
    slicelst = slicelist(b)
    b2 = np.array(b)
    if samplerate is None:
        samplerate = 1.0
    for sc in slicelst:
        dur = (sc.stop - sc.start) / samplerate
        if not eval(rule):
            b2[sc] = False
    return b2