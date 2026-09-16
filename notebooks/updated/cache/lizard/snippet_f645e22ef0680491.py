def speziale_grun(v, v0, gamma0, q0, q1):
    if isuncertainties([v, v0, gamma0, q0, q1]):
        gamma = gamma0 * unp.exp(q0 / q1 * ((v / v0) ** q1 - 1.0))
    else:
        gamma = gamma0 * np.exp(q0 / q1 * ((v / v0) ** q1 - 1.0))
    return gamma