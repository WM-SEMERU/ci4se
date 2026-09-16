def ispercolating(am, inlets, outlets, mode='site'):
    r
    if am.format is not 'coo':
        am = am.to_coo()
    ij = sp.vstack((am.col, am.row)).T
    if mode.startswith('site'):
        occupied_sites = sp.zeros(shape=am.shape[0], dtype=bool)
        occupied_sites[ij[am.data].flatten()] = True
        clusters = site_percolation(ij, occupied_sites)
    elif mode.startswith('bond'):
        occupied_bonds = am.data
        clusters = bond_percolation(ij, occupied_bonds)
    ins = sp.unique(clusters.sites[inlets])
    if ins[0] == -1:
        ins = ins[1:]
    outs = sp.unique(clusters.sites[outlets])
    if outs[0] == -1:
        outs = outs[1:]
    hits = sp.in1d(ins, outs)
    return sp.any(hits)