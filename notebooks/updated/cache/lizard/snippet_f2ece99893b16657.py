def _compute_C1_term(C, dists):
    c1_dists = np.zeros_like(dists)
    idx = dists < C['Rc11']
    c1_dists[idx] = C['phi_11']
    idx = (dists >= C['Rc11']) & (dists <= C['Rc21'])
    c1_dists[idx] = C['phi_11'] + (C['phi_21'] - C['phi_11']) * ((dists[idx
        ] - C['Rc11']) / (C['Rc21'] - C['Rc11']))
    idx = dists > C['Rc21']
    c1_dists[idx] = C['phi_21']
    return c1_dists