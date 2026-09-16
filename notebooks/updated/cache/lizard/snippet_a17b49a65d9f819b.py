def calc_gs_snu_ujy(b, ne, delta, sinth, width, elongation, dist, ghz):
    hz = ghz * 1000000000.0
    eta = calc_gs_eta(b, ne, delta, sinth, hz)
    kappa = calc_gs_kappa(b, ne, delta, sinth, hz)
    snu = calc_snu(eta, kappa, width, elongation, dist)
    ujy = snu * cgs.jypercgs * 1000000.0
    return ujy