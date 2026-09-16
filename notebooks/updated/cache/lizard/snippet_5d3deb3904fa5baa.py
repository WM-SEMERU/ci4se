def damping_after_dephasing(T1, T2, gate_time):
    assert T1 >= 0
    assert T2 >= 0
    if T1 != INFINITY:
        damping = damping_kraus_map(p=1 - np.exp(-float(gate_time) / float(T1))
            )
    else:
        damping = [np.eye(2)]
    if T2 != INFINITY:
        gamma_phi = float(gate_time) / float(T2)
        if T1 != INFINITY:
            if T2 > 2 * T1:
                raise ValueError('T2 is upper bounded by 2 * T1')
            gamma_phi -= float(gate_time) / float(2 * T1)
        dephasing = dephasing_kraus_map(p=0.5 * (1 - np.exp(-2 * gamma_phi)))
    else:
        dephasing = [np.eye(2)]
    return combine_kraus_maps(damping, dephasing)