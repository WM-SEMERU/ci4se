def observable(operator, rho, unfolding, complex=False):
    r
    if len(rho.shape) == 2:
        return np.array([observable(operator, i, unfolding) for i in rho])
    Ne = unfolding.Ne
    Mu = unfolding.Mu
    obs = 0
    if unfolding.normalized:
        rho11 = 1 - sum([rho[Mu(1, i, i)] for i in range(1, Ne)])
    for i in range(Ne):
        for k in range(Ne):
            if unfolding.real:
                if k == 0 and i == 0:
                    obs += operator[i, k] * rho11
                else:
                    if k < i:
                        u, v = i, k
                    else:
                        u, v = k, i
                    obs += operator[i, k] * rho[Mu(1, u, v)]
                    if k != i:
                        if k < i:
                            obs += 1.0j * operator[i, k] * rho[Mu(-1, u, v)]
                        else:
                            obs += -1.0j * operator[i, k] * rho[Mu(-1, u, v)]
            elif k == 0 and i == 0:
                obs += operator[i, k] * rho11
            else:
                obs += operator[i, k] * rho[Mu(0, k, i)]
    if not complex:
        obs = np.real(obs)
    return obs