def evolve_pn_spins(q, chiA0, chiB0, omega0, omegaTimesM_final, approximant
    ='SpinTaylorT4', dt=0.1, spinO=7, phaseO=7):
    omega, phi, chiA, chiB, lNhat, e1 = lal_spin_evloution_wrapper(approximant,
        q, omega0, chiA0, chiB0, dt, spinO, phaseO)
    end_idx = np.argmin(np.abs(omega - omegaTimesM_final))
    omegaTimesM_end = omega[end_idx]
    chiA_end = chiA[end_idx]
    chiB_end = chiB[end_idx]
    lNhat_end = lNhat[end_idx]
    phi_end = phi[end_idx]
    q_copr_end = _utils.alignVec_quat(lNhat_end)
    chiA_end_copr = _utils.transformTimeDependentVector(np.array([
        q_copr_end]).T, np.array([chiA_end]).T, inverse=1).T[0]
    chiB_end_copr = _utils.transformTimeDependentVector(np.array([
        q_copr_end]).T, np.array([chiB_end]).T, inverse=1).T[0]
    return chiA_end_copr, chiB_end_copr, q_copr_end, phi_end, omegaTimesM_end