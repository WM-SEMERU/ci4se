def mtie(data, rate=1.0, data_type='phase', taus=None):
    phase = input_to_phase(data, rate, data_type)
    phase, m, taus_used = tau_generator(phase, rate, taus)
    devs = np.zeros_like(taus_used)
    deverrs = np.zeros_like(taus_used)
    ns = np.zeros_like(taus_used)
    for idx, mj in enumerate(m):
        rw = mtie_rolling_window(phase, int(mj + 1))
        win_max = np.max(rw, axis=1)
        win_min = np.min(rw, axis=1)
        tie = win_max - win_min
        dev = np.max(tie)
        ncount = phase.shape[0] - mj
        devs[idx] = dev
        deverrs[idx] = dev / np.sqrt(ncount)
        ns[idx] = ncount
    return remove_small_ns(taus_used, devs, deverrs, ns)