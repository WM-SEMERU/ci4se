def get_BM_EOS(cryst, systems):
    pvdat = array([[r.get_volume(), get_pressure(r.get_stress()), norm(r.
        get_cell()[:, (0)]), norm(r.get_cell()[:, (1)]), norm(r.get_cell()[
        :, (2)])] for r in systems]).T
    v1 = min(pvdat[0])
    v2 = max(pvdat[0])
    p2 = min(pvdat[1])
    p1 = max(pvdat[1])
    b0 = (p1 * v1 - p2 * v2) / (v2 - v1)
    v0 = v1 * (p1 + b0) / b0
    p0 = [v0, b0, 1]
    try:
        p1, succ = optimize.curve_fit(BMEOS, pvdat[0], pvdat[1], p0)
    except (ValueError, RuntimeError, optimize.OptimizeWarning) as ex:
        raise RuntimeError('Calculation failed')
    cryst.bm_eos = p1
    cryst.pv = pvdat
    return cryst.bm_eos