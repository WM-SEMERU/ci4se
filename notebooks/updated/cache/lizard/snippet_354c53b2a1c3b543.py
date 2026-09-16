def get_objects(remove_dups=True, include_frames=False):
    gc.collect()
    tmp = gc.get_objects()
    tmp = [o for o in tmp if not isframe(o)]
    res = []
    for o in tmp:
        refs = get_referents(o)
        for ref in refs:
            if not _is_containerobject(ref):
                res.append(ref)
    res.extend(tmp)
    if remove_dups:
        res = _remove_duplicates(res)
    if include_frames:
        for sf in stack()[2:]:
            res.append(sf[0])
    return res