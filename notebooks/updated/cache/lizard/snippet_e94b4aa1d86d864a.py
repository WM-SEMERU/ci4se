def _get_fncsortnt(flds):
    if 'tinfo' in flds:
        return lambda ntgo: [ntgo.NS, -1 * ntgo.tinfo, ntgo.depth, ntgo.alt]
    if 'dcnt' in flds:
        return lambda ntgo: [ntgo.NS, -1 * ntgo.dcnt, ntgo.depth, ntgo.alt]
    return lambda ntgo: [ntgo.NS, -1 * ntgo.depth, ntgo.alt]