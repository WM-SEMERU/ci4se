def hybrid_meco_velocity(m1, m2, chi1, chi2, qm1=None, qm2=None):
    if qm1 is None:
        qm1 = 1
    if qm2 is None:
        qm2 = 1
    chi = (chi1 * m1 + chi2 * m2) / (m1 + m2)
    vmax = kerr_lightring_velocity(chi) - 0.01
    return minimize(hybridEnergy, 0.2, args=(m1, m2, chi1, chi2, qm1, qm2),
        bounds=[(0.1, vmax)]).x.item()