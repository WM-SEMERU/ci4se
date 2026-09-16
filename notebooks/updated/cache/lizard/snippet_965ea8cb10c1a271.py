def _get_colordata(bs, elements, bs_projection):
    contribs = {}
    if bs_projection and bs_projection.lower() == 'elements':
        projections = bs.get_projection_on_elements()
    for spin in (Spin.up, Spin.down):
        if spin in bs.bands:
            contribs[spin] = []
            for band_idx in range(bs.nb_bands):
                colors = []
                for k_idx in range(len(bs.kpoints)):
                    if bs_projection and bs_projection.lower() == 'elements':
                        c = [0, 0, 0]
                        projs = projections[spin][band_idx][k_idx]
                        projs = dict([(k, v ** 2) for k, v in projs.items()])
                        total = sum(projs.values())
                        if total > 0:
                            for idx, e in enumerate(elements):
                                c[idx] = math.sqrt(projs[e] / total)
                        c = [c[1], c[2], c[0]]
                    else:
                        c = [0, 0, 0] if spin == Spin.up else [0, 0, 1]
                    colors.append(c)
                contribs[spin].append(colors)
            contribs[spin] = np.array(contribs[spin])
    return contribs