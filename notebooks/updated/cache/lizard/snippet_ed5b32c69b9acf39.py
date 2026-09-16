def corrpix_deform_delta(area_um, px_um=0.34):
    pxcorr = (0.34 / px_um) ** 2
    offs = 0.0012
    exp1 = 0.02 * np.exp(-area_um * pxcorr / 7.1)
    exp2 = 0.01 * np.exp(-area_um * pxcorr / 38.6)
    exp3 = 0.005 * np.exp(-area_um * pxcorr / 296)
    delta = offs + exp1 + exp2 + exp3
    return delta