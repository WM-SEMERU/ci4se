def three_cornered_hat_phase(phasedata_ab, phasedata_bc, phasedata_ca, rate,
    taus, function):
    tau_ab, dev_ab, err_ab, ns_ab = function(phasedata_ab, data_type=
        'phase', rate=rate, taus=taus)
    tau_bc, dev_bc, err_bc, ns_bc = function(phasedata_bc, data_type=
        'phase', rate=rate, taus=taus)
    tau_ca, dev_ca, err_ca, ns_ca = function(phasedata_ca, data_type=
        'phase', rate=rate, taus=taus)
    var_ab = dev_ab * dev_ab
    var_bc = dev_bc * dev_bc
    var_ca = dev_ca * dev_ca
    assert len(var_ab) == len(var_bc) == len(var_ca)
    var_a = 0.5 * (var_ab + var_ca - var_bc)
    var_a[var_a < 0] = 0
    dev_a = np.sqrt(var_a)
    err_a = [(d / np.sqrt(nn)) for d, nn in zip(dev_a, ns_ab)]
    return tau_ab, dev_a, err_a, ns_ab